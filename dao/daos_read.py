import dao.dao_connection
from typing import TypeVar, Generic, List, Iterable
from dao.dao_base import base_dao
from dto.dtos import *
from dto.dtos_read import *
from dto.dtos_read_list import *
from dto.dtos_write import *
from dto.dtos_write_list import *
from dto.dtos_models import db_models

# auto-generated - DaoRead - STARD

class account_division_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.account_division_model
    def get_items(self, sql: str) -> list[account_division_read_dto]:
        return list(map(lambda r: account_division_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_division_read_dto]:
        return list(map(lambda r: account_division_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> account_division_read_dto | None:
        return account_division_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> account_division_read_dtos:
        return account_division_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_account_division_uid(self, col_value: any, n: int = 1000) -> account_division_read_dtos:
        return self.get_items_by_any_column('account_division_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> account_division_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_division_name(self, col_value: any, n: int = 1000) -> account_division_read_dtos:
        return self.get_items_by_any_column('division_name', col_value, n)
    def get_items_by_division_description(self, col_value: any, n: int = 1000) -> account_division_read_dtos:
        return self.get_items_by_any_column('division_description', col_value, n)
    def insert_dto(self, dto: account_division_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, account_division_uid: str , system_version_uid: str , division_name: str , division_description: str ) -> int:
        return self.insert_single(account_division_write_dto.new_write(account_division_uid, system_version_uid, division_name, division_description))
    def insert_row_random_uid(self, system_version_uid: str , division_name: str , division_description: str ) -> int:
        return self.insert_single(account_division_write_dto.new_write_random_uid(system_version_uid, division_name, division_description))
    def insert_dtos(self, dtos: list[account_division_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_division_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_division_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: account_division_write_dto, created_by: str = "system") -> account_division_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: account_division_write_dtos, created_by: str = "system") -> account_division_read_dtos:
        return account_division_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, account_division_uid: str , system_version_uid: str , division_name: str , division_description: str , updated_by: str="system") -> int:
        params = account_division_write_dto.new_write(account_division_uid, system_version_uid, division_name, division_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, account_division_uid: str , system_version_uid: str , division_name: str , division_description: str , updated_by: str = "system") -> account_division_read_dto | None:
        params = account_division_write_dto.new_write(account_division_uid, system_version_uid, division_name, division_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(account_division_uid)
    def delete_logical_dtos(self, dtos: list[account_division_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_division_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_group_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.account_group_model
    def get_items(self, sql: str) -> list[account_group_read_dto]:
        return list(map(lambda r: account_group_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_group_read_dto]:
        return list(map(lambda r: account_group_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> account_group_read_dto | None:
        return account_group_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> account_group_read_dtos:
        return account_group_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_account_group_uid(self, col_value: any, n: int = 1000) -> account_group_read_dtos:
        return self.get_items_by_any_column('account_group_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> account_group_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_account_group_name(self, col_value: any, n: int = 1000) -> account_group_read_dtos:
        return self.get_items_by_any_column('account_group_name', col_value, n)
    def get_items_by_account_group_description(self, col_value: any, n: int = 1000) -> account_group_read_dtos:
        return self.get_items_by_any_column('account_group_description', col_value, n)
    def insert_dto(self, dto: account_group_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, account_group_uid: str , system_version_uid: str , account_group_name: str , account_group_description: str ) -> int:
        return self.insert_single(account_group_write_dto.new_write(account_group_uid, system_version_uid, account_group_name, account_group_description))
    def insert_row_random_uid(self, system_version_uid: str , account_group_name: str , account_group_description: str ) -> int:
        return self.insert_single(account_group_write_dto.new_write_random_uid(system_version_uid, account_group_name, account_group_description))
    def insert_dtos(self, dtos: list[account_group_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_group_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_group_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: account_group_write_dto, created_by: str = "system") -> account_group_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: account_group_write_dtos, created_by: str = "system") -> account_group_read_dtos:
        return account_group_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, account_group_uid: str , system_version_uid: str , account_group_name: str , account_group_description: str , updated_by: str="system") -> int:
        params = account_group_write_dto.new_write(account_group_uid, system_version_uid, account_group_name, account_group_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, account_group_uid: str , system_version_uid: str , account_group_name: str , account_group_description: str , updated_by: str = "system") -> account_group_read_dto | None:
        params = account_group_write_dto.new_write(account_group_uid, system_version_uid, account_group_name, account_group_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(account_group_uid)
    def delete_logical_dtos(self, dtos: list[account_group_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_group_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.account_instance_model
    def get_items(self, sql: str) -> list[account_instance_read_dto]:
        return list(map(lambda r: account_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_instance_read_dto]:
        return list(map(lambda r: account_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> account_instance_read_dto | None:
        return account_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> account_instance_read_dtos:
        return account_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_account_type_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_type_uid', col_value, n)
    def get_items_by_account_title_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_title_uid', col_value, n)
    def get_items_by_account_division_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_division_uid', col_value, n)
    def get_items_by_account_group_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_group_uid', col_value, n)
    def get_items_by_auth_identity_uid(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('auth_identity_uid', col_value, n)
    def get_items_by_account_email(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_email', col_value, n)
    def get_items_by_account_name(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('account_name', col_value, n)
    def get_items_by_display_name(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('display_name', col_value, n)
    def get_items_by_is_system(self, col_value: any, n: int = 1000) -> account_instance_read_dtos:
        return self.get_items_by_any_column('is_system', col_value, n)
    def insert_dto(self, dto: account_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, account_instance_uid: str , client_instance_uid: str , account_type_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ) -> int:
        return self.insert_single(account_instance_write_dto.new_write(account_instance_uid, client_instance_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system))
    def insert_row_random_uid(self, client_instance_uid: str , account_type_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int ) -> int:
        return self.insert_single(account_instance_write_dto.new_write_random_uid(client_instance_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system))
    def insert_dtos(self, dtos: list[account_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: account_instance_write_dto, created_by: str = "system") -> account_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: account_instance_write_dtos, created_by: str = "system") -> account_instance_read_dtos:
        return account_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, account_instance_uid: str , client_instance_uid: str , account_type_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int , updated_by: str="system") -> int:
        params = account_instance_write_dto.new_write(account_instance_uid, client_instance_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, account_instance_uid: str , client_instance_uid: str , account_type_uid: str , account_title_uid: str , account_division_uid: str , account_group_uid: str , auth_identity_uid: str , account_email: str , account_name: str , display_name: str , is_system: int , updated_by: str = "system") -> account_instance_read_dto | None:
        params = account_instance_write_dto.new_write(account_instance_uid, client_instance_uid, account_type_uid, account_title_uid, account_division_uid, account_group_uid, auth_identity_uid, account_email, account_name, display_name, is_system).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(account_instance_uid)
    def delete_logical_dtos(self, dtos: list[account_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_title_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.account_title_model
    def get_items(self, sql: str) -> list[account_title_read_dto]:
        return list(map(lambda r: account_title_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_title_read_dto]:
        return list(map(lambda r: account_title_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> account_title_read_dto | None:
        return account_title_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> account_title_read_dtos:
        return account_title_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_account_title_uid(self, col_value: any, n: int = 1000) -> account_title_read_dtos:
        return self.get_items_by_any_column('account_title_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> account_title_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_title_name(self, col_value: any, n: int = 1000) -> account_title_read_dtos:
        return self.get_items_by_any_column('title_name', col_value, n)
    def get_items_by_title_description(self, col_value: any, n: int = 1000) -> account_title_read_dtos:
        return self.get_items_by_any_column('title_description', col_value, n)
    def insert_dto(self, dto: account_title_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, account_title_uid: str , system_version_uid: str , title_name: str , title_description: str ) -> int:
        return self.insert_single(account_title_write_dto.new_write(account_title_uid, system_version_uid, title_name, title_description))
    def insert_row_random_uid(self, system_version_uid: str , title_name: str , title_description: str ) -> int:
        return self.insert_single(account_title_write_dto.new_write_random_uid(system_version_uid, title_name, title_description))
    def insert_dtos(self, dtos: list[account_title_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_title_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_title_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: account_title_write_dto, created_by: str = "system") -> account_title_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: account_title_write_dtos, created_by: str = "system") -> account_title_read_dtos:
        return account_title_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, account_title_uid: str , system_version_uid: str , title_name: str , title_description: str , updated_by: str="system") -> int:
        params = account_title_write_dto.new_write(account_title_uid, system_version_uid, title_name, title_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, account_title_uid: str , system_version_uid: str , title_name: str , title_description: str , updated_by: str = "system") -> account_title_read_dto | None:
        params = account_title_write_dto.new_write(account_title_uid, system_version_uid, title_name, title_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(account_title_uid)
    def delete_logical_dtos(self, dtos: list[account_title_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_title_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class account_type_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.account_type_model
    def get_items(self, sql: str) -> list[account_type_read_dto]:
        return list(map(lambda r: account_type_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[account_type_read_dto]:
        return list(map(lambda r: account_type_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> account_type_read_dto | None:
        return account_type_read_dtos(self.get_items_with_params(sql, params)).get_first()
    def get_items_write(self, sql: str) -> list[account_type_write_dto]:
        return list(map(lambda r: account_type_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[account_type_write_dto]:
        return list(map(lambda r: account_type_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> account_type_write_dtos:
        return account_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> account_type_write_dtos:
        return account_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> account_type_write_dtos:
        return account_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> account_type_write_dtos:
        return account_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> account_type_read_dto | None:
        return account_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> account_type_read_dto | None:
        return account_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> account_type_read_dtos:
        return account_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_account_type_uid(self, col_value: any, n: int = 1000) -> account_type_read_dtos:
        return self.get_items_by_any_column('account_type_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> account_type_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_account_type_name(self, col_value: any, n: int = 1000) -> account_type_read_dtos:
        return self.get_items_by_any_column('account_type_name', col_value, n)
    def get_items_by_account_type_description(self, col_value: any, n: int = 1000) -> account_type_read_dtos:
        return self.get_items_by_any_column('account_type_description', col_value, n)
    def insert_dto(self, dto: account_type_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, account_type_uid: str , system_version_uid: str , account_type_name: str , account_type_description: str ) -> int:
        return self.insert_single(account_type_write_dto.new_write(account_type_uid, system_version_uid, account_type_name, account_type_description))
    def insert_row_random_uid(self, system_version_uid: str , account_type_name: str , account_type_description: str ) -> int:
        return self.insert_single(account_type_write_dto.new_write_random_uid(system_version_uid, account_type_name, account_type_description))
    def insert_dtos(self, dtos: list[account_type_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: account_type_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: account_type_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: account_type_write_dto, created_by: str = "system") -> account_type_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: account_type_write_dtos, created_by: str = "system") -> account_type_read_dtos:
        return account_type_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, account_type_uid: str , system_version_uid: str , account_type_name: str , account_type_description: str , updated_by: str="system") -> int:
        params = account_type_write_dto.new_write(account_type_uid, system_version_uid, account_type_name, account_type_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, account_type_uid: str , system_version_uid: str , account_type_name: str , account_type_description: str , updated_by: str = "system") -> account_type_read_dto | None:
        params = account_type_write_dto.new_write(account_type_uid, system_version_uid, account_type_name, account_type_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(account_type_uid)
    def delete_logical_dtos(self, dtos: list[account_type_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: account_type_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_identity_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_identity_model
    def get_items(self, sql: str) -> list[auth_identity_read_dto]:
        return list(map(lambda r: auth_identity_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_identity_read_dto]:
        return list(map(lambda r: auth_identity_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_identity_read_dto | None:
        return auth_identity_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_identity_read_dtos:
        return auth_identity_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_identity_uid(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('auth_identity_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_identity_name(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('identity_name', col_value, n)
    def get_items_by_identity_type(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('identity_type', col_value, n)
    def get_items_by_identity_parameters(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('identity_parameters', col_value, n)
    def get_items_by_last_status_name(self, col_value: any, n: int = 1000) -> auth_identity_read_dtos:
        return self.get_items_by_any_column('last_status_name', col_value, n)
    def insert_dto(self, dto: auth_identity_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_identity_uid: str , client_instance_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ) -> int:
        return self.insert_single(auth_identity_write_dto.new_write(auth_identity_uid, client_instance_uid, identity_name, identity_type, identity_parameters, last_status_name))
    def insert_row_random_uid(self, client_instance_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str ) -> int:
        return self.insert_single(auth_identity_write_dto.new_write_random_uid(client_instance_uid, identity_name, identity_type, identity_parameters, last_status_name))
    def insert_dtos(self, dtos: list[auth_identity_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_identity_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_identity_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_identity_write_dto, created_by: str = "system") -> auth_identity_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_identity_write_dtos, created_by: str = "system") -> auth_identity_read_dtos:
        return auth_identity_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_identity_uid: str , client_instance_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str , updated_by: str="system") -> int:
        params = auth_identity_write_dto.new_write(auth_identity_uid, client_instance_uid, identity_name, identity_type, identity_parameters, last_status_name).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_identity_uid: str , client_instance_uid: str , identity_name: str , identity_type: str , identity_parameters: str , last_status_name: str , updated_by: str = "system") -> auth_identity_read_dto | None:
        params = auth_identity_write_dto.new_write(auth_identity_uid, client_instance_uid, identity_name, identity_type, identity_parameters, last_status_name).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_identity_uid)
    def delete_logical_dtos(self, dtos: list[auth_identity_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_identity_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_password_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_password_model
    def get_items(self, sql: str) -> list[auth_password_read_dto]:
        return list(map(lambda r: auth_password_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_password_read_dto]:
        return list(map(lambda r: auth_password_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_password_read_dto | None:
        return auth_password_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_password_read_dtos:
        return auth_password_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_password_uid(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('auth_password_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_password_hash(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('password_hash', col_value, n)
    def get_items_by_password_salt(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('password_salt', col_value, n)
    def get_items_by_date_from(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('date_from', col_value, n)
    def get_items_by_date_to(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('date_to', col_value, n)
    def get_items_by_usage_count(self, col_value: any, n: int = 1000) -> auth_password_read_dtos:
        return self.get_items_by_any_column('usage_count', col_value, n)
    def insert_dto(self, dto: auth_password_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_password_uid: str , account_instance_uid: str , system_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ) -> int:
        return self.insert_single(auth_password_write_dto.new_write(auth_password_uid, account_instance_uid, system_instance_uid, password_hash, password_salt, date_from, date_to, usage_count))
    def insert_row_random_uid(self, account_instance_uid: str , system_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int ) -> int:
        return self.insert_single(auth_password_write_dto.new_write_random_uid(account_instance_uid, system_instance_uid, password_hash, password_salt, date_from, date_to, usage_count))
    def insert_dtos(self, dtos: list[auth_password_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_password_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_password_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_password_write_dto, created_by: str = "system") -> auth_password_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_password_write_dtos, created_by: str = "system") -> auth_password_read_dtos:
        return auth_password_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_password_uid: str , account_instance_uid: str , system_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int , updated_by: str="system") -> int:
        params = auth_password_write_dto.new_write(auth_password_uid, account_instance_uid, system_instance_uid, password_hash, password_salt, date_from, date_to, usage_count).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_password_uid: str , account_instance_uid: str , system_instance_uid: str , password_hash: str , password_salt: str , date_from: datetime.datetime , date_to: datetime.datetime , usage_count: int , updated_by: str = "system") -> auth_password_read_dto | None:
        params = auth_password_write_dto.new_write(auth_password_uid, account_instance_uid, system_instance_uid, password_hash, password_salt, date_from, date_to, usage_count).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_password_uid)
    def delete_logical_dtos(self, dtos: list[auth_password_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_password_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_permission_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_permission_model
    def get_items(self, sql: str) -> list[auth_permission_read_dto]:
        return list(map(lambda r: auth_permission_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_permission_read_dto]:
        return list(map(lambda r: auth_permission_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_permission_read_dto | None:
        return auth_permission_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_permission_read_dtos:
        return auth_permission_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_permission_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('auth_permission_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_auth_role_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('auth_role_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_valid_from_date(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('valid_from_date', col_value, n)
    def get_items_by_valid_till_date(self, col_value: any, n: int = 1000) -> auth_permission_read_dtos:
        return self.get_items_by_any_column('valid_till_date', col_value, n)
    def insert_dto(self, dto: auth_permission_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_permission_uid: str , account_instance_uid: str , system_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ) -> int:
        return self.insert_single(auth_permission_write_dto.new_write(auth_permission_uid, account_instance_uid, system_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date))
    def insert_row_random_uid(self, account_instance_uid: str , system_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime ) -> int:
        return self.insert_single(auth_permission_write_dto.new_write_random_uid(account_instance_uid, system_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date))
    def insert_dtos(self, dtos: list[auth_permission_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_permission_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_permission_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_permission_write_dto, created_by: str = "system") -> auth_permission_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_permission_write_dtos, created_by: str = "system") -> auth_permission_read_dtos:
        return auth_permission_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_permission_uid: str , account_instance_uid: str , system_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime , updated_by: str="system") -> int:
        params = auth_permission_write_dto.new_write(auth_permission_uid, account_instance_uid, system_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_permission_uid: str , account_instance_uid: str , system_instance_uid: str , auth_role_uid: str , client_instance_uid: str  | None, project_instance_uid: str  | None, valid_from_date: datetime.datetime , valid_till_date: datetime.datetime , updated_by: str = "system") -> auth_permission_read_dto | None:
        params = auth_permission_write_dto.new_write(auth_permission_uid, account_instance_uid, system_instance_uid, auth_role_uid, client_instance_uid, project_instance_uid, valid_from_date, valid_till_date).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_permission_uid)
    def delete_logical_dtos(self, dtos: list[auth_permission_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_permission_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_request_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_request_model
    def get_items(self, sql: str) -> list[auth_request_read_dto]:
        return list(map(lambda r: auth_request_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_request_read_dto]:
        return list(map(lambda r: auth_request_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_request_read_dto | None:
        return auth_request_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_request_read_dtos:
        return auth_request_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_request_uid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('auth_request_uid', col_value, n)
    def get_items_by_by_account_instance_uid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('by_account_instance_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_reset_guid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('reset_guid', col_value, n)
    def get_items_by_valid_till_date(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('valid_till_date', col_value, n)
    def get_items_by_lock_guid(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('lock_guid', col_value, n)
    def get_items_by_lock_by(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('lock_by', col_value, n)
    def get_items_by_lock_date(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('lock_date', col_value, n)
    def get_items_by_is_checked(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('is_checked', col_value, n)
    def get_items_by_is_used(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('is_used', col_value, n)
    def get_items_by_check_date(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('check_date', col_value, n)
    def get_items_by_use_date(self, col_value: any, n: int = 1000) -> auth_request_read_dtos:
        return self.get_items_by_any_column('use_date', col_value, n)
    def insert_dto(self, dto: auth_request_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , system_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None) -> int:
        return self.insert_single(auth_request_write_dto.new_write(auth_request_uid, by_account_instance_uid, account_instance_uid, system_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date))
    def insert_row_random_uid(self, by_account_instance_uid: str , account_instance_uid: str , system_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None) -> int:
        return self.insert_single(auth_request_write_dto.new_write_random_uid(by_account_instance_uid, account_instance_uid, system_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date))
    def insert_dtos(self, dtos: list[auth_request_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_request_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_request_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_request_write_dto, created_by: str = "system") -> auth_request_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_request_write_dtos, created_by: str = "system") -> auth_request_read_dtos:
        return auth_request_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , system_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None, updated_by: str="system") -> int:
        params = auth_request_write_dto.new_write(auth_request_uid, by_account_instance_uid, account_instance_uid, system_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_request_uid: str , by_account_instance_uid: str , account_instance_uid: str , system_instance_uid: str , reset_guid: str , valid_till_date: datetime.datetime , lock_guid: str  | None, lock_by: str  | None, lock_date: datetime.datetime  | None, is_checked: int , is_used: int , check_date: datetime.datetime  | None, use_date: datetime.datetime  | None, updated_by: str = "system") -> auth_request_read_dto | None:
        params = auth_request_write_dto.new_write(auth_request_uid, by_account_instance_uid, account_instance_uid, system_instance_uid, reset_guid, valid_till_date, lock_guid, lock_by, lock_date, is_checked, is_used, check_date, use_date).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_request_uid)
    def delete_logical_dtos(self, dtos: list[auth_request_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_request_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_role_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_role_model
    def get_items(self, sql: str) -> list[auth_role_read_dto]:
        return list(map(lambda r: auth_role_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_role_read_dto]:
        return list(map(lambda r: auth_role_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_role_read_dto | None:
        return auth_role_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_role_read_dtos:
        return auth_role_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_role_uid(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('auth_role_uid', col_value, n)
    def get_items_by_parent_auth_role_uid(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('parent_auth_role_uid', col_value, n)
    def get_items_by_role_name(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('role_name', col_value, n)
    def get_items_by_role_description(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('role_description', col_value, n)
    def get_items_by_access_uris(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('access_uris', col_value, n)
    def get_items_by_is_project(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('is_project', col_value, n)
    def get_items_by_is_client(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('is_client', col_value, n)
    def get_items_by_is_custom(self, col_value: any, n: int = 1000) -> auth_role_read_dtos:
        return self.get_items_by_any_column('is_custom', col_value, n)
    def insert_dto(self, dto: auth_role_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ) -> int:
        return self.insert_single(auth_role_write_dto.new_write(auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom))
    def insert_row_random_uid(self, parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int ) -> int:
        return self.insert_single(auth_role_write_dto.new_write_random_uid(parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom))
    def insert_dtos(self, dtos: list[auth_role_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_role_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_role_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_role_write_dto, created_by: str = "system") -> auth_role_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_role_write_dtos, created_by: str = "system") -> auth_role_read_dtos:
        return auth_role_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int , updated_by: str="system") -> int:
        params = auth_role_write_dto.new_write(auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_role_uid: str , parent_auth_role_uid: str  | None, role_name: str , role_description: str , access_uris: str , is_project: int , is_client: int , is_custom: int , updated_by: str = "system") -> auth_role_read_dto | None:
        params = auth_role_write_dto.new_write(auth_role_uid, parent_auth_role_uid, role_name, role_description, access_uris, is_project, is_client, is_custom).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_role_uid)
    def delete_logical_dtos(self, dtos: list[auth_role_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_role_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class auth_token_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.auth_token_model
    def get_items(self, sql: str) -> list[auth_token_read_dto]:
        return list(map(lambda r: auth_token_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[auth_token_read_dto]:
        return list(map(lambda r: auth_token_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> auth_token_read_dto | None:
        return auth_token_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> auth_token_read_dtos:
        return auth_token_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_auth_token_uid(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('auth_token_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_token_seq(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('token_seq', col_value, n)
    def get_items_by_token_hash(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('token_hash', col_value, n)
    def get_items_by_token_salt(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('token_salt', col_value, n)
    def get_items_by_valid_till_date(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('valid_till_date', col_value, n)
    def get_items_by_last_use_date(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('last_use_date', col_value, n)
    def get_items_by_is_last(self, col_value: any, n: int = 1000) -> auth_token_read_dtos:
        return self.get_items_by_any_column('is_last', col_value, n)
    def insert_dto(self, dto: auth_token_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, auth_token_uid: str , account_instance_uid: str , system_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ) -> int:
        return self.insert_single(auth_token_write_dto.new_write(auth_token_uid, account_instance_uid, system_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last))
    def insert_row_random_uid(self, account_instance_uid: str , system_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int ) -> int:
        return self.insert_single(auth_token_write_dto.new_write_random_uid(account_instance_uid, system_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last))
    def insert_dtos(self, dtos: list[auth_token_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: auth_token_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: auth_token_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: auth_token_write_dto, created_by: str = "system") -> auth_token_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: auth_token_write_dtos, created_by: str = "system") -> auth_token_read_dtos:
        return auth_token_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, auth_token_uid: str , account_instance_uid: str , system_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int , updated_by: str="system") -> int:
        params = auth_token_write_dto.new_write(auth_token_uid, account_instance_uid, system_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, auth_token_uid: str , account_instance_uid: str , system_instance_uid: str , token_seq: int , token_hash: str , token_salt: str , valid_till_date: datetime.datetime  | None, last_use_date: datetime.datetime  | None, is_last: int , updated_by: str = "system") -> auth_token_read_dto | None:
        params = auth_token_write_dto.new_write(auth_token_uid, account_instance_uid, system_instance_uid, token_seq, token_hash, token_salt, valid_till_date, last_use_date, is_last).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(auth_token_uid)
    def delete_logical_dtos(self, dtos: list[auth_token_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: auth_token_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class client_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.client_instance_model
    def get_items(self, sql: str) -> list[client_instance_read_dto]:
        return list(map(lambda r: client_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[client_instance_read_dto]:
        return list(map(lambda r: client_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> client_instance_read_dto | None:
        return client_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> client_instance_read_dtos:
        return client_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_country_uid(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('country_uid', col_value, n)
    def get_items_by_client_name(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('client_name', col_value, n)
    def get_items_by_client_code(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('client_code', col_value, n)
    def get_items_by_client_description(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('client_description', col_value, n)
    def get_items_by_start_date(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('start_date', col_value, n)
    def get_items_by_end_date(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('end_date', col_value, n)
    def get_items_by_is_internal(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('is_internal', col_value, n)
    def get_items_by_is_system(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('is_system', col_value, n)
    def get_items_by_is_test(self, col_value: any, n: int = 1000) -> client_instance_read_dtos:
        return self.get_items_by_any_column('is_test', col_value, n)
    def insert_dto(self, dto: client_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ) -> int:
        return self.insert_single(client_instance_write_dto.new_write(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test))
    def insert_row_random_uid(self, country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int ) -> int:
        return self.insert_single(client_instance_write_dto.new_write_random_uid(country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test))
    def insert_dtos(self, dtos: list[client_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: client_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: client_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: client_instance_write_dto, created_by: str = "system") -> client_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: client_instance_write_dtos, created_by: str = "system") -> client_instance_read_dtos:
        return client_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int , updated_by: str="system") -> int:
        params = client_instance_write_dto.new_write(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, client_instance_uid: str , country_uid: str , client_name: str , client_code: str , client_description: str , start_date: datetime.datetime , end_date: datetime.datetime  | None, is_internal: int , is_system: int , is_test: int , updated_by: str = "system") -> client_instance_read_dto | None:
        params = client_instance_write_dto.new_write(client_instance_uid, country_uid, client_name, client_code, client_description, start_date, end_date, is_internal, is_system, is_test).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(client_instance_uid)
    def delete_logical_dtos(self, dtos: list[client_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: client_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class client_type_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.client_type_model
    def get_items(self, sql: str) -> list[client_type_read_dto]:
        return list(map(lambda r: client_type_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[client_type_read_dto]:
        return list(map(lambda r: client_type_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> client_type_read_dto | None:
        return client_type_read_dtos(self.get_items_with_params(sql, params)).get_first()
    def get_items_write(self, sql: str) -> list[client_type_write_dto]:
        return list(map(lambda r: client_type_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[client_type_write_dto]:
        return list(map(lambda r: client_type_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> client_type_write_dtos:
        return client_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> client_type_write_dtos:
        return client_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> client_type_write_dtos:
        return client_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> client_type_write_dtos:
        return client_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> client_type_read_dto | None:
        return client_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> client_type_read_dto | None:
        return client_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> client_type_read_dtos:
        return client_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_client_type_uid(self, col_value: any, n: int = 1000) -> client_type_read_dtos:
        return self.get_items_by_any_column('client_type_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> client_type_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_client_type_name(self, col_value: any, n: int = 1000) -> client_type_read_dtos:
        return self.get_items_by_any_column('client_type_name', col_value, n)
    def insert_dto(self, dto: client_type_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, client_type_uid: str , system_version_uid: str , client_type_name: str ) -> int:
        return self.insert_single(client_type_write_dto.new_write(client_type_uid, system_version_uid, client_type_name))
    def insert_row_random_uid(self, system_version_uid: str , client_type_name: str ) -> int:
        return self.insert_single(client_type_write_dto.new_write_random_uid(system_version_uid, client_type_name))
    def insert_dtos(self, dtos: list[client_type_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: client_type_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: client_type_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: client_type_write_dto, created_by: str = "system") -> client_type_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: client_type_write_dtos, created_by: str = "system") -> client_type_read_dtos:
        return client_type_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, client_type_uid: str , system_version_uid: str , client_type_name: str , updated_by: str="system") -> int:
        params = client_type_write_dto.new_write(client_type_uid, system_version_uid, client_type_name).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, client_type_uid: str , system_version_uid: str , client_type_name: str , updated_by: str = "system") -> client_type_read_dto | None:
        params = client_type_write_dto.new_write(client_type_uid, system_version_uid, client_type_name).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(client_type_uid)
    def delete_logical_dtos(self, dtos: list[client_type_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: client_type_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class country_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.country_model
    def get_items(self, sql: str) -> list[country_read_dto]:
        return list(map(lambda r: country_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[country_read_dto]:
        return list(map(lambda r: country_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> country_read_dtos:
        return country_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> country_read_dto | None:
        return country_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> country_read_dtos:
        return country_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_country_uid(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('country_uid', col_value, n)
    def get_items_by_continent_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('continent_name', col_value, n)
    def get_items_by_continent_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('continent_code', col_value, n)
    def get_items_by_country_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('country_name', col_value, n)
    def get_items_by_country_iso3(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('country_iso3', col_value, n)
    def get_items_by_country_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('country_code', col_value, n)
    def get_items_by_phone_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('phone_code', col_value, n)
    def get_items_by_currency_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('currency_code', col_value, n)
    def get_items_by_capital_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('capital_name', col_value, n)
    def get_items_by_region_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('region_name', col_value, n)
    def get_items_by_subregion_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('subregion_name', col_value, n)
    def get_items_by_region_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('region_code', col_value, n)
    def get_items_by_latitude(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('latitude', col_value, n)
    def get_items_by_longitude(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('longitude', col_value, n)
    def get_items_by_currency_name(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('currency_name', col_value, n)
    def get_items_by_population(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('population', col_value, n)
    def get_items_by_languages(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('languages', col_value, n)
    def get_items_by_area(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('area', col_value, n)
    def get_items_by_bar_code(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('bar_code', col_value, n)
    def get_items_by_top_level_domain(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('top_level_domain', col_value, n)
    def get_items_by_is_focused(self, col_value: any, n: int = 1000) -> country_read_dtos:
        return self.get_items_by_any_column('is_focused', col_value, n)
    def insert_dto(self, dto: country_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ) -> int:
        return self.insert_single(country_write_dto.new_write(country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused))
    def insert_row_random_uid(self, continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int ) -> int:
        return self.insert_single(country_write_dto.new_write_random_uid(continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused))
    def insert_dtos(self, dtos: list[country_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: country_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: country_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: country_write_dto, created_by: str = "system") -> country_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: country_write_dtos, created_by: str = "system") -> country_read_dtos:
        return country_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int , updated_by: str="system") -> int:
        params = country_write_dto.new_write(country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, country_uid: str , continent_name: str , continent_code: str , country_name: str , country_iso3: str , country_code: str , phone_code: str , currency_code: str , capital_name: str , region_name: str , subregion_name: str , region_code: str , latitude: str , longitude: str , currency_name: str , population: str , languages: str , area: str , bar_code: str , top_level_domain: str , is_focused: int , updated_by: str = "system") -> country_read_dto | None:
        params = country_write_dto.new_write(country_uid, continent_name, continent_code, country_name, country_iso3, country_code, phone_code, currency_code, capital_name, region_name, subregion_name, region_code, latitude, longitude, currency_name, population, languages, area, bar_code, top_level_domain, is_focused).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(country_uid)
    def delete_logical_dtos(self, dtos: list[country_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: country_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class currency_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.currency_model
    def get_items(self, sql: str) -> list[currency_read_dto]:
        return list(map(lambda r: currency_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[currency_read_dto]:
        return list(map(lambda r: currency_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> currency_read_dtos:
        return currency_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> currency_read_dto | None:
        return currency_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> currency_read_dtos:
        return currency_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_currency_uid(self, col_value: any, n: int = 1000) -> currency_read_dtos:
        return self.get_items_by_any_column('currency_uid', col_value, n)
    def get_items_by_currency_name(self, col_value: any, n: int = 1000) -> currency_read_dtos:
        return self.get_items_by_any_column('currency_name', col_value, n)
    def get_items_by_is_focused(self, col_value: any, n: int = 1000) -> currency_read_dtos:
        return self.get_items_by_any_column('is_focused', col_value, n)
    def insert_dto(self, dto: currency_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, currency_uid: str , currency_name: str , is_focused: int ) -> int:
        return self.insert_single(currency_write_dto.new_write(currency_uid, currency_name, is_focused))
    def insert_row_random_uid(self, currency_name: str , is_focused: int ) -> int:
        return self.insert_single(currency_write_dto.new_write_random_uid(currency_name, is_focused))
    def insert_dtos(self, dtos: list[currency_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: currency_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: currency_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: currency_write_dto, created_by: str = "system") -> currency_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: currency_write_dtos, created_by: str = "system") -> currency_read_dtos:
        return currency_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, currency_uid: str , currency_name: str , is_focused: int , updated_by: str="system") -> int:
        params = currency_write_dto.new_write(currency_uid, currency_name, is_focused).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, currency_uid: str , currency_name: str , is_focused: int , updated_by: str = "system") -> currency_read_dto | None:
        params = currency_write_dto.new_write(currency_uid, currency_name, is_focused).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(currency_uid)
    def delete_logical_dtos(self, dtos: list[currency_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: currency_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class entry_final_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.entry_final_model
    def get_items(self, sql: str) -> list[entry_final_read_dto]:
        return list(map(lambda r: entry_final_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[entry_final_read_dto]:
        return list(map(lambda r: entry_final_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> entry_final_read_dto | None:
        return entry_final_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> entry_final_read_dtos:
        return entry_final_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_entry_final_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('entry_final_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_project_milestone_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('project_milestone_uid', col_value, n)
    def get_items_by_invoice_instance_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('invoice_instance_uid', col_value, n)
    def get_items_by_entry_period(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('entry_period', col_value, n)
    def get_items_by_entry_note(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('entry_note', col_value, n)
    def get_items_by_lock_uid(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('lock_uid', col_value, n)
    def get_items_by_start_date(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('start_date', col_value, n)
    def get_items_by_end_date(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('end_date', col_value, n)
    def get_items_by_entry_minutes(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('entry_minutes', col_value, n)
    def get_items_by_is_approved(self, col_value: any, n: int = 1000) -> entry_final_read_dtos:
        return self.get_items_by_any_column('is_approved', col_value, n)
    def insert_dto(self, dto: entry_final_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ) -> int:
        return self.insert_single(entry_final_write_dto.new_write(entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved))
    def insert_row_random_uid(self, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ) -> int:
        return self.insert_single(entry_final_write_dto.new_write_random_uid(account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved))
    def insert_dtos(self, dtos: list[entry_final_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: entry_final_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: entry_final_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: entry_final_write_dto, created_by: str = "system") -> entry_final_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: entry_final_write_dtos, created_by: str = "system") -> entry_final_read_dtos:
        return entry_final_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , updated_by: str="system") -> int:
        params = entry_final_write_dto.new_write(entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, entry_final_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , updated_by: str = "system") -> entry_final_read_dto | None:
        params = entry_final_write_dto.new_write(entry_final_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(entry_final_uid)
    def delete_logical_dtos(self, dtos: list[entry_final_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: entry_final_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class entry_save_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.entry_save_model
    def get_items(self, sql: str) -> list[entry_save_read_dto]:
        return list(map(lambda r: entry_save_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[entry_save_read_dto]:
        return list(map(lambda r: entry_save_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> entry_save_read_dto | None:
        return entry_save_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> entry_save_read_dtos:
        return entry_save_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_entry_save_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('entry_save_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_project_milestone_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('project_milestone_uid', col_value, n)
    def get_items_by_invoice_instance_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('invoice_instance_uid', col_value, n)
    def get_items_by_entry_period(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('entry_period', col_value, n)
    def get_items_by_entry_note(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('entry_note', col_value, n)
    def get_items_by_lock_uid(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('lock_uid', col_value, n)
    def get_items_by_start_date(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('start_date', col_value, n)
    def get_items_by_end_date(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('end_date', col_value, n)
    def get_items_by_entry_minutes(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('entry_minutes', col_value, n)
    def get_items_by_is_approved(self, col_value: any, n: int = 1000) -> entry_save_read_dtos:
        return self.get_items_by_any_column('is_approved', col_value, n)
    def insert_dto(self, dto: entry_save_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ) -> int:
        return self.insert_single(entry_save_write_dto.new_write(entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved))
    def insert_row_random_uid(self, account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int ) -> int:
        return self.insert_single(entry_save_write_dto.new_write_random_uid(account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved))
    def insert_dtos(self, dtos: list[entry_save_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: entry_save_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: entry_save_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: entry_save_write_dto, created_by: str = "system") -> entry_save_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: entry_save_write_dtos, created_by: str = "system") -> entry_save_read_dtos:
        return entry_save_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , updated_by: str="system") -> int:
        params = entry_save_write_dto.new_write(entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, entry_save_uid: str , account_instance_uid: str , project_instance_uid: str , project_milestone_uid: str , invoice_instance_uid: str  | None, entry_period: str , entry_note: str , lock_uid: str  | None, start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, entry_minutes: int , is_approved: int , updated_by: str = "system") -> entry_save_read_dto | None:
        params = entry_save_write_dto.new_write(entry_save_uid, account_instance_uid, project_instance_uid, project_milestone_uid, invoice_instance_uid, entry_period, entry_note, lock_uid, start_date, end_date, entry_minutes, is_approved).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(entry_save_uid)
    def delete_logical_dtos(self, dtos: list[entry_save_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: entry_save_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_channel_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.event_channel_model
    def get_items(self, sql: str) -> list[event_channel_read_dto]:
        return list(map(lambda r: event_channel_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_channel_read_dto]:
        return list(map(lambda r: event_channel_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> event_channel_read_dto | None:
        return event_channel_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> event_channel_read_dtos:
        return event_channel_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_event_channel_uid(self, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return self.get_items_by_any_column('event_channel_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_channel_type(self, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return self.get_items_by_any_column('channel_type', col_value, n)
    def get_items_by_channel_name(self, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return self.get_items_by_any_column('channel_name', col_value, n)
    def get_items_by_channel_definition(self, col_value: any, n: int = 1000) -> event_channel_read_dtos:
        return self.get_items_by_any_column('channel_definition', col_value, n)
    def insert_dto(self, dto: event_channel_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, event_channel_uid: str , system_version_uid: str , channel_type: str , channel_name: str , channel_definition: str ) -> int:
        return self.insert_single(event_channel_write_dto.new_write(event_channel_uid, system_version_uid, channel_type, channel_name, channel_definition))
    def insert_row_random_uid(self, system_version_uid: str , channel_type: str , channel_name: str , channel_definition: str ) -> int:
        return self.insert_single(event_channel_write_dto.new_write_random_uid(system_version_uid, channel_type, channel_name, channel_definition))
    def insert_dtos(self, dtos: list[event_channel_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_channel_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_channel_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: event_channel_write_dto, created_by: str = "system") -> event_channel_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: event_channel_write_dtos, created_by: str = "system") -> event_channel_read_dtos:
        return event_channel_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, event_channel_uid: str , system_version_uid: str , channel_type: str , channel_name: str , channel_definition: str , updated_by: str="system") -> int:
        params = event_channel_write_dto.new_write(event_channel_uid, system_version_uid, channel_type, channel_name, channel_definition).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, event_channel_uid: str , system_version_uid: str , channel_type: str , channel_name: str , channel_definition: str , updated_by: str = "system") -> event_channel_read_dto | None:
        params = event_channel_write_dto.new_write(event_channel_uid, system_version_uid, channel_type, channel_name, channel_definition).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(event_channel_uid)
    def delete_logical_dtos(self, dtos: list[event_channel_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_channel_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.event_instance_model
    def get_items(self, sql: str) -> list[event_instance_read_dto]:
        return list(map(lambda r: event_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_instance_read_dto]:
        return list(map(lambda r: event_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> event_instance_read_dto | None:
        return event_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> event_instance_read_dtos:
        return event_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_event_instance_uid(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_event_type(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_type', col_value, n)
    def get_items_by_event_object(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_object', col_value, n)
    def get_items_by_event_method(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_method', col_value, n)
    def get_items_by_event_parameters(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_parameters', col_value, n)
    def get_items_by_event_signature(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_signature', col_value, n)
    def get_items_by_published_count(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('published_count', col_value, n)
    def get_items_by_event_date(self, col_value: any, n: int = 1000) -> event_instance_read_dtos:
        return self.get_items_by_any_column('event_date', col_value, n)
    def insert_dto(self, dto: event_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, event_instance_uid: str , system_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ) -> int:
        return self.insert_single(event_instance_write_dto.new_write(event_instance_uid, system_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date))
    def insert_row_random_uid(self, system_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime ) -> int:
        return self.insert_single(event_instance_write_dto.new_write_random_uid(system_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date))
    def insert_dtos(self, dtos: list[event_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: event_instance_write_dto, created_by: str = "system") -> event_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: event_instance_write_dtos, created_by: str = "system") -> event_instance_read_dtos:
        return event_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, event_instance_uid: str , system_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime , updated_by: str="system") -> int:
        params = event_instance_write_dto.new_write(event_instance_uid, system_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, event_instance_uid: str , system_instance_uid: str , event_type: str , event_object: str , event_method: str , event_parameters: str , event_signature: str , published_count: int , event_date: datetime.datetime , updated_by: str = "system") -> event_instance_read_dto | None:
        params = event_instance_write_dto.new_write(event_instance_uid, system_instance_uid, event_type, event_object, event_method, event_parameters, event_signature, published_count, event_date).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(event_instance_uid)
    def delete_logical_dtos(self, dtos: list[event_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class event_subscription_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.event_subscription_model
    def get_items(self, sql: str) -> list[event_subscription_read_dto]:
        return list(map(lambda r: event_subscription_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[event_subscription_read_dto]:
        return list(map(lambda r: event_subscription_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> event_subscription_read_dto | None:
        return event_subscription_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> event_subscription_read_dtos:
        return event_subscription_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_event_subscription_uid(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('event_subscription_uid', col_value, n)
    def get_items_by_event_channel_uid(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('event_channel_uid', col_value, n)
    def get_items_by_subscription_name(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('subscription_name', col_value, n)
    def get_items_by_subscription_filter(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('subscription_filter', col_value, n)
    def get_items_by_subscription_topic(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('subscription_topic', col_value, n)
    def get_items_by_subscription_template(self, col_value: any, n: int = 1000) -> event_subscription_read_dtos:
        return self.get_items_by_any_column('subscription_template', col_value, n)
    def insert_dto(self, dto: event_subscription_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ) -> int:
        return self.insert_single(event_subscription_write_dto.new_write(event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template))
    def insert_row_random_uid(self, event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str ) -> int:
        return self.insert_single(event_subscription_write_dto.new_write_random_uid(event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template))
    def insert_dtos(self, dtos: list[event_subscription_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: event_subscription_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: event_subscription_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: event_subscription_write_dto, created_by: str = "system") -> event_subscription_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: event_subscription_write_dtos, created_by: str = "system") -> event_subscription_read_dtos:
        return event_subscription_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str , updated_by: str="system") -> int:
        params = event_subscription_write_dto.new_write(event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, event_subscription_uid: str , event_channel_uid: str , subscription_name: str , subscription_filter: str , subscription_topic: str , subscription_template: str , updated_by: str = "system") -> event_subscription_read_dto | None:
        params = event_subscription_write_dto.new_write(event_subscription_uid, event_channel_uid, subscription_name, subscription_filter, subscription_topic, subscription_template).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(event_subscription_uid)
    def delete_logical_dtos(self, dtos: list[event_subscription_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: event_subscription_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class invoice_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.invoice_instance_model
    def get_items(self, sql: str) -> list[invoice_instance_read_dto]:
        return list(map(lambda r: invoice_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[invoice_instance_read_dto]:
        return list(map(lambda r: invoice_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> invoice_instance_read_dto | None:
        return invoice_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_invoice_instance_uid(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_instance_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_period_code(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('period_code', col_value, n)
    def get_items_by_invoice_number(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_number', col_value, n)
    def get_items_by_invoice_details(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_details', col_value, n)
    def get_items_by_invoice_status(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_status', col_value, n)
    def get_items_by_invoice_currency(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_currency', col_value, n)
    def get_items_by_invoice_amount(self, col_value: any, n: int = 1000) -> invoice_instance_read_dtos:
        return self.get_items_by_any_column('invoice_amount', col_value, n)
    def insert_dto(self, dto: invoice_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ) -> int:
        return self.insert_single(invoice_instance_write_dto.new_write(invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount))
    def insert_row_random_uid(self, client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str ) -> int:
        return self.insert_single(invoice_instance_write_dto.new_write_random_uid(client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount))
    def insert_dtos(self, dtos: list[invoice_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: invoice_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: invoice_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: invoice_instance_write_dto, created_by: str = "system") -> invoice_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: invoice_instance_write_dtos, created_by: str = "system") -> invoice_instance_read_dtos:
        return invoice_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str , updated_by: str="system") -> int:
        params = invoice_instance_write_dto.new_write(invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, invoice_instance_uid: str , client_instance_uid: str , account_instance_uid: str , period_code: str , invoice_number: str , invoice_details: str , invoice_status: str , invoice_currency: str , invoice_amount: str , updated_by: str = "system") -> invoice_instance_read_dto | None:
        params = invoice_instance_write_dto.new_write(invoice_instance_uid, client_instance_uid, account_instance_uid, period_code, invoice_number, invoice_details, invoice_status, invoice_currency, invoice_amount).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(invoice_instance_uid)
    def delete_logical_dtos(self, dtos: list[invoice_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: invoice_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class notification_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.notification_instance_model
    def get_items(self, sql: str) -> list[notification_instance_read_dto]:
        return list(map(lambda r: notification_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[notification_instance_read_dto]:
        return list(map(lambda r: notification_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> notification_instance_read_dto | None:
        return notification_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> notification_instance_read_dtos:
        return notification_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_notification_instance_uid(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('notification_instance_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_notification_type(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('notification_type', col_value, n)
    def get_items_by_notification_topic(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('notification_topic', col_value, n)
    def get_items_by_notification_format(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('notification_format', col_value, n)
    def get_items_by_notification_content(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('notification_content', col_value, n)
    def get_items_by_sending_status(self, col_value: any, n: int = 1000) -> notification_instance_read_dtos:
        return self.get_items_by_any_column('sending_status', col_value, n)
    def insert_dto(self, dto: notification_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, notification_instance_uid: str , client_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ) -> int:
        return self.insert_single(notification_instance_write_dto.new_write(notification_instance_uid, client_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status))
    def insert_row_random_uid(self, client_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str ) -> int:
        return self.insert_single(notification_instance_write_dto.new_write_random_uid(client_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status))
    def insert_dtos(self, dtos: list[notification_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: notification_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: notification_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: notification_instance_write_dto, created_by: str = "system") -> notification_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: notification_instance_write_dtos, created_by: str = "system") -> notification_instance_read_dtos:
        return notification_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, notification_instance_uid: str , client_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str , updated_by: str="system") -> int:
        params = notification_instance_write_dto.new_write(notification_instance_uid, client_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, notification_instance_uid: str , client_instance_uid: str , account_instance_uid: str , notification_type: str , notification_topic: str , notification_format: str , notification_content: str , sending_status: str , updated_by: str = "system") -> notification_instance_read_dto | None:
        params = notification_instance_write_dto.new_write(notification_instance_uid, client_instance_uid, account_instance_uid, notification_type, notification_topic, notification_format, notification_content, sending_status).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(notification_instance_uid)
    def delete_logical_dtos(self, dtos: list[notification_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: notification_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_budget_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.project_budget_model
    def get_items(self, sql: str) -> list[project_budget_read_dto]:
        return list(map(lambda r: project_budget_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_budget_read_dto]:
        return list(map(lambda r: project_budget_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> project_budget_read_dto | None:
        return project_budget_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> project_budget_read_dtos:
        return project_budget_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_project_budget_uid(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('project_budget_uid', col_value, n)
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_budget_name(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('budget_name', col_value, n)
    def get_items_by_budget_currency(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('budget_currency', col_value, n)
    def get_items_by_budget_value(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('budget_value', col_value, n)
    def get_items_by_is_current(self, col_value: any, n: int = 1000) -> project_budget_read_dtos:
        return self.get_items_by_any_column('is_current', col_value, n)
    def insert_dto(self, dto: project_budget_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ) -> int:
        return self.insert_single(project_budget_write_dto.new_write(project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current))
    def insert_row_random_uid(self, project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int ) -> int:
        return self.insert_single(project_budget_write_dto.new_write_random_uid(project_instance_uid, budget_name, budget_currency, budget_value, is_current))
    def insert_dtos(self, dtos: list[project_budget_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_budget_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_budget_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: project_budget_write_dto, created_by: str = "system") -> project_budget_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: project_budget_write_dtos, created_by: str = "system") -> project_budget_read_dtos:
        return project_budget_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int , updated_by: str="system") -> int:
        params = project_budget_write_dto.new_write(project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, project_budget_uid: str , project_instance_uid: str , budget_name: str , budget_currency: str , budget_value: str , is_current: int , updated_by: str = "system") -> project_budget_read_dto | None:
        params = project_budget_write_dto.new_write(project_budget_uid, project_instance_uid, budget_name, budget_currency, budget_value, is_current).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(project_budget_uid)
    def delete_logical_dtos(self, dtos: list[project_budget_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_budget_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_group_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.project_group_model
    def get_items(self, sql: str) -> list[project_group_read_dto]:
        return list(map(lambda r: project_group_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_group_read_dto]:
        return list(map(lambda r: project_group_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> project_group_read_dto | None:
        return project_group_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> project_group_read_dtos:
        return project_group_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_project_group_uid(self, col_value: any, n: int = 1000) -> project_group_read_dtos:
        return self.get_items_by_any_column('project_group_uid', col_value, n)
    def get_items_by_project_group_name(self, col_value: any, n: int = 1000) -> project_group_read_dtos:
        return self.get_items_by_any_column('project_group_name', col_value, n)
    def get_items_by_project_group_description(self, col_value: any, n: int = 1000) -> project_group_read_dtos:
        return self.get_items_by_any_column('project_group_description', col_value, n)
    def insert_dto(self, dto: project_group_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, project_group_uid: str , project_group_name: str , project_group_description: str ) -> int:
        return self.insert_single(project_group_write_dto.new_write(project_group_uid, project_group_name, project_group_description))
    def insert_row_random_uid(self, project_group_name: str , project_group_description: str ) -> int:
        return self.insert_single(project_group_write_dto.new_write_random_uid(project_group_name, project_group_description))
    def insert_dtos(self, dtos: list[project_group_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_group_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_group_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: project_group_write_dto, created_by: str = "system") -> project_group_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: project_group_write_dtos, created_by: str = "system") -> project_group_read_dtos:
        return project_group_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, project_group_uid: str , project_group_name: str , project_group_description: str , updated_by: str="system") -> int:
        params = project_group_write_dto.new_write(project_group_uid, project_group_name, project_group_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, project_group_uid: str , project_group_name: str , project_group_description: str , updated_by: str = "system") -> project_group_read_dto | None:
        params = project_group_write_dto.new_write(project_group_uid, project_group_name, project_group_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(project_group_uid)
    def delete_logical_dtos(self, dtos: list[project_group_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_group_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.project_instance_model
    def get_items(self, sql: str) -> list[project_instance_read_dto]:
        return list(map(lambda r: project_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_instance_read_dto]:
        return list(map(lambda r: project_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> project_instance_read_dto | None:
        return project_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> project_instance_read_dtos:
        return project_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_client_instance_uid(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('client_instance_uid', col_value, n)
    def get_items_by_manager_account_instance_uid(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('manager_account_instance_uid', col_value, n)
    def get_items_by_project_group_uid(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('project_group_uid', col_value, n)
    def get_items_by_project_name(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('project_name', col_value, n)
    def get_items_by_project_code(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('project_code', col_value, n)
    def get_items_by_is_billable(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('is_billable', col_value, n)
    def get_items_by_start_date(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('start_date', col_value, n)
    def get_items_by_end_date(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('end_date', col_value, n)
    def get_items_by_current_billed(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('current_billed', col_value, n)
    def get_items_by_budget(self, col_value: any, n: int = 1000) -> project_instance_read_dtos:
        return self.get_items_by_any_column('budget', col_value, n)
    def insert_dto(self, dto: project_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ) -> int:
        return self.insert_single(project_instance_write_dto.new_write(project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget))
    def insert_row_random_uid(self, client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str ) -> int:
        return self.insert_single(project_instance_write_dto.new_write_random_uid(client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget))
    def insert_dtos(self, dtos: list[project_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: project_instance_write_dto, created_by: str = "system") -> project_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: project_instance_write_dtos, created_by: str = "system") -> project_instance_read_dtos:
        return project_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str , updated_by: str="system") -> int:
        params = project_instance_write_dto.new_write(project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, project_instance_uid: str , client_instance_uid: str , manager_account_instance_uid: str , project_group_uid: str , project_name: str , project_code: str , is_billable: int , start_date: datetime.datetime  | None, end_date: datetime.datetime  | None, current_billed: str , budget: str , updated_by: str = "system") -> project_instance_read_dto | None:
        params = project_instance_write_dto.new_write(project_instance_uid, client_instance_uid, manager_account_instance_uid, project_group_uid, project_name, project_code, is_billable, start_date, end_date, current_billed, budget).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(project_instance_uid)
    def delete_logical_dtos(self, dtos: list[project_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class project_milestone_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.project_milestone_model
    def get_items(self, sql: str) -> list[project_milestone_read_dto]:
        return list(map(lambda r: project_milestone_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[project_milestone_read_dto]:
        return list(map(lambda r: project_milestone_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> project_milestone_read_dto | None:
        return project_milestone_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> project_milestone_read_dtos:
        return project_milestone_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_project_milestone_uid(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('project_milestone_uid', col_value, n)
    def get_items_by_project_instance_uid(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('project_instance_uid', col_value, n)
    def get_items_by_project_budget_uid(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('project_budget_uid', col_value, n)
    def get_items_by_milestone_name(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('milestone_name', col_value, n)
    def get_items_by_start_date(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('start_date', col_value, n)
    def get_items_by_end_date(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('end_date', col_value, n)
    def get_items_by_status_name(self, col_value: any, n: int = 1000) -> project_milestone_read_dtos:
        return self.get_items_by_any_column('status_name', col_value, n)
    def insert_dto(self, dto: project_milestone_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ) -> int:
        return self.insert_single(project_milestone_write_dto.new_write(project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name))
    def insert_row_random_uid(self, project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str ) -> int:
        return self.insert_single(project_milestone_write_dto.new_write_random_uid(project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name))
    def insert_dtos(self, dtos: list[project_milestone_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: project_milestone_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: project_milestone_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: project_milestone_write_dto, created_by: str = "system") -> project_milestone_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: project_milestone_write_dtos, created_by: str = "system") -> project_milestone_read_dtos:
        return project_milestone_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str , updated_by: str="system") -> int:
        params = project_milestone_write_dto.new_write(project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, project_milestone_uid: str , project_instance_uid: str , project_budget_uid: str  | None, milestone_name: str , start_date: datetime.datetime , end_date: datetime.datetime , status_name: str , updated_by: str = "system") -> project_milestone_read_dto | None:
        params = project_milestone_write_dto.new_write(project_milestone_uid, project_instance_uid, project_budget_uid, milestone_name, start_date, end_date, status_name).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(project_milestone_uid)
    def delete_logical_dtos(self, dtos: list[project_milestone_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: project_milestone_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_attribute_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_attribute_model
    def get_items(self, sql: str) -> list[system_attribute_read_dto]:
        return list(map(lambda r: system_attribute_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_attribute_read_dto]:
        return list(map(lambda r: system_attribute_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_attribute_read_dto | None:
        return system_attribute_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_attribute_read_dtos:
        return system_attribute_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_attribute_uid(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('system_attribute_uid', col_value, n)
    def get_items_by_system_object_uid(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('system_object_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_column_name(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('column_name', col_value, n)
    def get_items_by_attribute_name(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('attribute_name', col_value, n)
    def get_items_by_attribute_type(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('attribute_type', col_value, n)
    def get_items_by_attribute_label(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('attribute_label', col_value, n)
    def get_items_by_attribute_description(self, col_value: any, n: int = 1000) -> system_attribute_read_dtos:
        return self.get_items_by_any_column('attribute_description', col_value, n)
    def insert_dto(self, dto: system_attribute_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_attribute_uid: str , system_object_uid: str , system_version_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ) -> int:
        return self.insert_single(system_attribute_write_dto.new_write(system_attribute_uid, system_object_uid, system_version_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description))
    def insert_row_random_uid(self, system_object_uid: str , system_version_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str ) -> int:
        return self.insert_single(system_attribute_write_dto.new_write_random_uid(system_object_uid, system_version_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description))
    def insert_dtos(self, dtos: list[system_attribute_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_attribute_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_attribute_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_attribute_write_dto, created_by: str = "system") -> system_attribute_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_attribute_write_dtos, created_by: str = "system") -> system_attribute_read_dtos:
        return system_attribute_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_attribute_uid: str , system_object_uid: str , system_version_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str , updated_by: str="system") -> int:
        params = system_attribute_write_dto.new_write(system_attribute_uid, system_object_uid, system_version_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_attribute_uid: str , system_object_uid: str , system_version_uid: str , column_name: str , attribute_name: str , attribute_type: str , attribute_label: str , attribute_description: str , updated_by: str = "system") -> system_attribute_read_dto | None:
        params = system_attribute_write_dto.new_write(system_attribute_uid, system_object_uid, system_version_uid, column_name, attribute_name, attribute_type, attribute_label, attribute_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_attribute_uid)
    def delete_logical_dtos(self, dtos: list[system_attribute_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_attribute_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_change_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_change_model
    def get_items(self, sql: str) -> list[system_change_read_dto]:
        return list(map(lambda r: system_change_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_change_read_dto]:
        return list(map(lambda r: system_change_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_change_read_dto | None:
        return system_change_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_change_read_dtos:
        return system_change_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_change_uid(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('system_change_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_change_type(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('change_type', col_value, n)
    def get_items_by_change_name(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('change_name', col_value, n)
    def get_items_by_change_json(self, col_value: any, n: int = 1000) -> system_change_read_dtos:
        return self.get_items_by_any_column('change_json', col_value, n)
    def insert_dto(self, dto: system_change_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_change_uid: str , account_instance_uid: str , system_instance_uid: str , change_type: str , change_name: str , change_json: str ) -> int:
        return self.insert_single(system_change_write_dto.new_write(system_change_uid, account_instance_uid, system_instance_uid, change_type, change_name, change_json))
    def insert_row_random_uid(self, account_instance_uid: str , system_instance_uid: str , change_type: str , change_name: str , change_json: str ) -> int:
        return self.insert_single(system_change_write_dto.new_write_random_uid(account_instance_uid, system_instance_uid, change_type, change_name, change_json))
    def insert_dtos(self, dtos: list[system_change_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_change_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_change_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_change_write_dto, created_by: str = "system") -> system_change_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_change_write_dtos, created_by: str = "system") -> system_change_read_dtos:
        return system_change_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_change_uid: str , account_instance_uid: str , system_instance_uid: str , change_type: str , change_name: str , change_json: str , updated_by: str="system") -> int:
        params = system_change_write_dto.new_write(system_change_uid, account_instance_uid, system_instance_uid, change_type, change_name, change_json).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_change_uid: str , account_instance_uid: str , system_instance_uid: str , change_type: str , change_name: str , change_json: str , updated_by: str = "system") -> system_change_read_dto | None:
        params = system_change_write_dto.new_write(system_change_uid, account_instance_uid, system_instance_uid, change_type, change_name, change_json).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_change_uid)
    def delete_logical_dtos(self, dtos: list[system_change_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_change_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_database_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_database_model
    def get_items(self, sql: str) -> list[system_database_read_dto]:
        return list(map(lambda r: system_database_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_database_read_dto]:
        return list(map(lambda r: system_database_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_database_read_dto | None:
        return system_database_read_dtos(self.get_items_with_params(sql, params)).get_first()
    def get_items_write(self, sql: str) -> list[system_database_write_dto]:
        return list(map(lambda r: system_database_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_database_write_dto]:
        return list(map(lambda r: system_database_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_database_write_dtos:
        return system_database_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_database_write_dtos:
        return system_database_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_database_write_dtos:
        return system_database_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_database_write_dtos:
        return system_database_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_database_read_dto | None:
        return system_database_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_database_read_dto | None:
        return system_database_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_database_read_dtos:
        return system_database_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_database_uid(self, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return self.get_items_by_any_column('system_database_uid', col_value, n)
    def get_items_by_db_url(self, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return self.get_items_by_any_column('db_url', col_value, n)
    def get_items_by_db_host(self, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return self.get_items_by_any_column('db_host', col_value, n)
    def get_items_by_db_name(self, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return self.get_items_by_any_column('db_name', col_value, n)
    def get_items_by_db_user(self, col_value: any, n: int = 1000) -> system_database_read_dtos:
        return self.get_items_by_any_column('db_user', col_value, n)
    def insert_dto(self, dto: system_database_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_database_uid: str , db_url: str , db_host: str , db_name: str , db_user: str ) -> int:
        return self.insert_single(system_database_write_dto.new_write(system_database_uid, db_url, db_host, db_name, db_user))
    def insert_row_random_uid(self, db_url: str , db_host: str , db_name: str , db_user: str ) -> int:
        return self.insert_single(system_database_write_dto.new_write_random_uid(db_url, db_host, db_name, db_user))
    def insert_dtos(self, dtos: list[system_database_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_database_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_database_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_database_write_dto, created_by: str = "system") -> system_database_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_database_write_dtos, created_by: str = "system") -> system_database_read_dtos:
        return system_database_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_database_uid: str , db_url: str , db_host: str , db_name: str , db_user: str , updated_by: str="system") -> int:
        params = system_database_write_dto.new_write(system_database_uid, db_url, db_host, db_name, db_user).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_database_uid: str , db_url: str , db_host: str , db_name: str , db_user: str , updated_by: str = "system") -> system_database_read_dto | None:
        params = system_database_write_dto.new_write(system_database_uid, db_url, db_host, db_name, db_user).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_database_uid)
    def delete_logical_dtos(self, dtos: list[system_database_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_database_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_exception_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_exception_model
    def get_items(self, sql: str) -> list[system_exception_read_dto]:
        return list(map(lambda r: system_exception_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_exception_read_dto]:
        return list(map(lambda r: system_exception_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_exception_read_dto | None:
        return system_exception_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_exception_read_dtos:
        return system_exception_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_exception_uid(self, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return self.get_items_by_any_column('system_exception_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_exception_class(self, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return self.get_items_by_any_column('exception_class', col_value, n)
    def get_items_by_exception_message(self, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return self.get_items_by_any_column('exception_message', col_value, n)
    def get_items_by_exception_stacktrace(self, col_value: any, n: int = 1000) -> system_exception_read_dtos:
        return self.get_items_by_any_column('exception_stacktrace', col_value, n)
    def insert_dto(self, dto: system_exception_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ) -> int:
        return self.insert_single(system_exception_write_dto.new_write(system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace))
    def insert_row_random_uid(self, system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str ) -> int:
        return self.insert_single(system_exception_write_dto.new_write_random_uid(system_instance_uid, exception_class, exception_message, exception_stacktrace))
    def insert_dtos(self, dtos: list[system_exception_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_exception_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_exception_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_exception_write_dto, created_by: str = "system") -> system_exception_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_exception_write_dtos, created_by: str = "system") -> system_exception_read_dtos:
        return system_exception_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str , updated_by: str="system") -> int:
        params = system_exception_write_dto.new_write(system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_exception_uid: str , system_instance_uid: str , exception_class: str , exception_message: str , exception_stacktrace: str , updated_by: str = "system") -> system_exception_read_dto | None:
        params = system_exception_write_dto.new_write(system_exception_uid, system_instance_uid, exception_class, exception_message, exception_stacktrace).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_exception_uid)
    def delete_logical_dtos(self, dtos: list[system_exception_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_exception_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_instance_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_instance_model
    def get_items(self, sql: str) -> list[system_instance_read_dto]:
        return list(map(lambda r: system_instance_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_instance_read_dto]:
        return list(map(lambda r: system_instance_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_instance_read_dto | None:
        return system_instance_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_instance_read_dtos:
        return system_instance_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_host_name(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('host_name', col_value, n)
    def get_items_by_host_ip(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('host_ip', col_value, n)
    def get_items_by_local_path(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('local_path', col_value, n)
    def get_items_by_mode_name(self, col_value: any, n: int = 1000) -> system_instance_read_dtos:
        return self.get_items_by_any_column('mode_name', col_value, n)
    def insert_dto(self, dto: system_instance_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_instance_uid: str , system_version_uid: str , host_name: str , host_ip: str , local_path: str , mode_name: str ) -> int:
        return self.insert_single(system_instance_write_dto.new_write(system_instance_uid, system_version_uid, host_name, host_ip, local_path, mode_name))
    def insert_row_random_uid(self, system_version_uid: str , host_name: str , host_ip: str , local_path: str , mode_name: str ) -> int:
        return self.insert_single(system_instance_write_dto.new_write_random_uid(system_version_uid, host_name, host_ip, local_path, mode_name))
    def insert_dtos(self, dtos: list[system_instance_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_instance_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_instance_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_instance_write_dto, created_by: str = "system") -> system_instance_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_instance_write_dtos, created_by: str = "system") -> system_instance_read_dtos:
        return system_instance_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_instance_uid: str , system_version_uid: str , host_name: str , host_ip: str , local_path: str , mode_name: str , updated_by: str="system") -> int:
        params = system_instance_write_dto.new_write(system_instance_uid, system_version_uid, host_name, host_ip, local_path, mode_name).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_instance_uid: str , system_version_uid: str , host_name: str , host_ip: str , local_path: str , mode_name: str , updated_by: str = "system") -> system_instance_read_dto | None:
        params = system_instance_write_dto.new_write(system_instance_uid, system_version_uid, host_name, host_ip, local_path, mode_name).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_instance_uid)
    def delete_logical_dtos(self, dtos: list[system_instance_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_instance_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_object_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_object_model
    def get_items(self, sql: str) -> list[system_object_read_dto]:
        return list(map(lambda r: system_object_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_object_read_dto]:
        return list(map(lambda r: system_object_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_object_read_dto | None:
        return system_object_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_object_read_dtos:
        return system_object_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_object_uid(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('system_object_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_object_name(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('object_name', col_value, n)
    def get_items_by_object_type(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('object_type', col_value, n)
    def get_items_by_table_name(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('table_name', col_value, n)
    def get_items_by_key_name(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('key_name', col_value, n)
    def get_items_by_parent_system_object_uid(self, col_value: any, n: int = 1000) -> system_object_read_dtos:
        return self.get_items_by_any_column('parent_system_object_uid', col_value, n)
    def insert_dto(self, dto: system_object_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_object_uid: str , system_version_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None) -> int:
        return self.insert_single(system_object_write_dto.new_write(system_object_uid, system_version_uid, object_name, object_type, table_name, key_name, parent_system_object_uid))
    def insert_row_random_uid(self, system_version_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None) -> int:
        return self.insert_single(system_object_write_dto.new_write_random_uid(system_version_uid, object_name, object_type, table_name, key_name, parent_system_object_uid))
    def insert_dtos(self, dtos: list[system_object_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_object_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_object_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_object_write_dto, created_by: str = "system") -> system_object_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_object_write_dtos, created_by: str = "system") -> system_object_read_dtos:
        return system_object_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_object_uid: str , system_version_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None, updated_by: str="system") -> int:
        params = system_object_write_dto.new_write(system_object_uid, system_version_uid, object_name, object_type, table_name, key_name, parent_system_object_uid).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_object_uid: str , system_version_uid: str , object_name: str , object_type: str , table_name: str , key_name: str , parent_system_object_uid: str  | None, updated_by: str = "system") -> system_object_read_dto | None:
        params = system_object_write_dto.new_write(system_object_uid, system_version_uid, object_name, object_type, table_name, key_name, parent_system_object_uid).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_object_uid)
    def delete_logical_dtos(self, dtos: list[system_object_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_object_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_object_type_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_object_type_model
    def get_items(self, sql: str) -> list[system_object_type_read_dto]:
        return list(map(lambda r: system_object_type_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_object_type_read_dto]:
        return list(map(lambda r: system_object_type_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_object_type_read_dto | None:
        return system_object_type_read_dtos(self.get_items_with_params(sql, params)).get_first()
    def get_items_write(self, sql: str) -> list[system_object_type_write_dto]:
        return list(map(lambda r: system_object_type_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_object_type_write_dto]:
        return list(map(lambda r: system_object_type_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_object_type_write_dtos:
        return system_object_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_object_type_write_dtos:
        return system_object_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_object_type_write_dtos:
        return system_object_type_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_object_type_write_dtos:
        return system_object_type_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_object_type_read_dto | None:
        return system_object_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_object_type_read_dto | None:
        return system_object_type_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_object_type_read_dtos:
        return system_object_type_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_object_type_uid(self, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return self.get_items_by_any_column('system_object_type_uid', col_value, n)
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_system_object_uid(self, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return self.get_items_by_any_column('system_object_uid', col_value, n)
    def get_items_by_object_type_name(self, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return self.get_items_by_any_column('object_type_name', col_value, n)
    def get_items_by_object_type_description(self, col_value: any, n: int = 1000) -> system_object_type_read_dtos:
        return self.get_items_by_any_column('object_type_description', col_value, n)
    def insert_dto(self, dto: system_object_type_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_object_type_uid: str , system_version_uid: str , system_object_uid: str , object_type_name: str , object_type_description: str ) -> int:
        return self.insert_single(system_object_type_write_dto.new_write(system_object_type_uid, system_version_uid, system_object_uid, object_type_name, object_type_description))
    def insert_row_random_uid(self, system_version_uid: str , system_object_uid: str , object_type_name: str , object_type_description: str ) -> int:
        return self.insert_single(system_object_type_write_dto.new_write_random_uid(system_version_uid, system_object_uid, object_type_name, object_type_description))
    def insert_dtos(self, dtos: list[system_object_type_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_object_type_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_object_type_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_object_type_write_dto, created_by: str = "system") -> system_object_type_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_object_type_write_dtos, created_by: str = "system") -> system_object_type_read_dtos:
        return system_object_type_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_object_type_uid: str , system_version_uid: str , system_object_uid: str , object_type_name: str , object_type_description: str , updated_by: str="system") -> int:
        params = system_object_type_write_dto.new_write(system_object_type_uid, system_version_uid, system_object_uid, object_type_name, object_type_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_object_type_uid: str , system_version_uid: str , system_object_uid: str , object_type_name: str , object_type_description: str , updated_by: str = "system") -> system_object_type_read_dto | None:
        params = system_object_type_write_dto.new_write(system_object_type_uid, system_version_uid, system_object_uid, object_type_name, object_type_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_object_type_uid)
    def delete_logical_dtos(self, dtos: list[system_object_type_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_object_type_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_setting_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_setting_model
    def get_items(self, sql: str) -> list[system_setting_read_dto]:
        return list(map(lambda r: system_setting_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_setting_read_dto]:
        return list(map(lambda r: system_setting_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_setting_read_dto | None:
        return system_setting_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_setting_read_dtos:
        return system_setting_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_setting_uid(self, col_value: any, n: int = 1000) -> system_setting_read_dtos:
        return self.get_items_by_any_column('system_setting_uid', col_value, n)
    def get_items_by_account_instance_uid(self, col_value: any, n: int = 1000) -> system_setting_read_dtos:
        return self.get_items_by_any_column('account_instance_uid', col_value, n)
    def get_items_by_setting_name(self, col_value: any, n: int = 1000) -> system_setting_read_dtos:
        return self.get_items_by_any_column('setting_name', col_value, n)
    def get_items_by_setting_value(self, col_value: any, n: int = 1000) -> system_setting_read_dtos:
        return self.get_items_by_any_column('setting_value', col_value, n)
    def insert_dto(self, dto: system_setting_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str ) -> int:
        return self.insert_single(system_setting_write_dto.new_write(system_setting_uid, account_instance_uid, setting_name, setting_value))
    def insert_row_random_uid(self, account_instance_uid: str  | None, setting_name: str , setting_value: str ) -> int:
        return self.insert_single(system_setting_write_dto.new_write_random_uid(account_instance_uid, setting_name, setting_value))
    def insert_dtos(self, dtos: list[system_setting_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_setting_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_setting_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_setting_write_dto, created_by: str = "system") -> system_setting_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_setting_write_dtos, created_by: str = "system") -> system_setting_read_dtos:
        return system_setting_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str , updated_by: str="system") -> int:
        params = system_setting_write_dto.new_write(system_setting_uid, account_instance_uid, setting_name, setting_value).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_setting_uid: str , account_instance_uid: str  | None, setting_name: str , setting_value: str , updated_by: str = "system") -> system_setting_read_dto | None:
        params = system_setting_write_dto.new_write(system_setting_uid, account_instance_uid, setting_name, setting_value).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_setting_uid)
    def delete_logical_dtos(self, dtos: list[system_setting_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_setting_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_state_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_state_model
    def get_items(self, sql: str) -> list[system_state_read_dto]:
        return list(map(lambda r: system_state_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_state_read_dto]:
        return list(map(lambda r: system_state_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_state_read_dto | None:
        return system_state_read_dtos(self.get_items_with_params(sql, params)).get_first()
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
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_state_read_dtos:
        return system_state_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_state_uid(self, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return self.get_items_by_any_column('system_state_uid', col_value, n)
    def get_items_by_system_instance_uid(self, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return self.get_items_by_any_column('system_instance_uid', col_value, n)
    def get_items_by_mem_free(self, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return self.get_items_by_any_column('mem_free', col_value, n)
    def get_items_by_mem_max(self, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return self.get_items_by_any_column('mem_max', col_value, n)
    def get_items_by_objects_count(self, col_value: any, n: int = 1000) -> system_state_read_dtos:
        return self.get_items_by_any_column('objects_count', col_value, n)
    def insert_dto(self, dto: system_state_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_state_uid: str , system_instance_uid: str , mem_free: int , mem_max: int , objects_count: int ) -> int:
        return self.insert_single(system_state_write_dto.new_write(system_state_uid, system_instance_uid, mem_free, mem_max, objects_count))
    def insert_row_random_uid(self, system_instance_uid: str , mem_free: int , mem_max: int , objects_count: int ) -> int:
        return self.insert_single(system_state_write_dto.new_write_random_uid(system_instance_uid, mem_free, mem_max, objects_count))
    def insert_dtos(self, dtos: list[system_state_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_state_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_state_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_state_write_dto, created_by: str = "system") -> system_state_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_state_write_dtos, created_by: str = "system") -> system_state_read_dtos:
        return system_state_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_state_uid: str , system_instance_uid: str , mem_free: int , mem_max: int , objects_count: int , updated_by: str="system") -> int:
        params = system_state_write_dto.new_write(system_state_uid, system_instance_uid, mem_free, mem_max, objects_count).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_state_uid: str , system_instance_uid: str , mem_free: int , mem_max: int , objects_count: int , updated_by: str = "system") -> system_state_read_dto | None:
        params = system_state_write_dto.new_write(system_state_uid, system_instance_uid, mem_free, mem_max, objects_count).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_state_uid)
    def delete_logical_dtos(self, dtos: list[system_state_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_state_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)


class system_version_dao(base_dao):
    def __init__(self):
        super().__init__()
    def get_model(self) -> base_model:
        return db_models.system_version_model
    def get_items(self, sql: str) -> list[system_version_read_dto]:
        return list(map(lambda r: system_version_read_dto(*r), self.get_objects(sql)))
    def get_items_with_params(self, sql: str, params: Iterable) -> list[system_version_read_dto]:
        return list(map(lambda r: system_version_read_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_dtos(self, sql: str, params: Iterable = []) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items_with_params(sql, params))
    def get_item_dto_first(self, sql: str, params: Iterable = []) -> system_version_read_dto | None:
        return system_version_read_dtos(self.get_items_with_params(sql, params)).get_first()
    def get_items_write(self, sql: str) -> list[system_version_write_dto]:
        return list(map(lambda r: system_version_write_dto(*r), self.get_objects(sql)))
    def get_items_write_with_params(self, sql: str, params: Iterable) -> list[system_version_write_dto]:
        return list(map(lambda r: system_version_write_dto(*r), self.get_objects_by_params(sql, params)))
    def get_items_all(self, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items(self.get_model().get_select_all_limit_sql(n)))
    def get_items_active(self, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items(self.get_model().get_select_active_limit_sql(n)))
    def get_items_all_latest(self, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items(self.get_model().get_select_all_latest_sql(n)))
    def get_items_active_latest(self, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items(self.get_model().get_select_active_latest_sql(n)))
    def get_items_write_all(self, n: int = 1000) -> system_version_write_dtos:
        return system_version_write_dtos(self.get_items_write(self.get_model().get_select_write_all_limit_sql(n)))
    def get_items_write_active(self, n: int = 1000) -> system_version_write_dtos:
        return system_version_write_dtos(self.get_items_write(self.get_model().get_select_write_active_limit_sql(n)))
    def get_items_write_all_latest(self, n: int = 1000) -> system_version_write_dtos:
        return system_version_write_dtos(self.get_items_write(self.get_model().get_select_write_all_latest_sql(n)))
    def get_items_write_active_latest(self, n: int = 1000) -> system_version_write_dtos:
        return system_version_write_dtos(self.get_items_write(self.get_model().get_select_write_active_latest_sql(n)))
    def get_item_by_uid(self, uid: str) -> system_version_read_dto | None:
        return system_version_read_dtos(self.get_items_with_params(self.get_model().get_select_by_key(), (uid,))).get_first()
    def get_item_by_id(self, id: int) -> system_version_read_dto | None:
        return system_version_read_dtos(self.get_items_with_params(self.get_model().get_select_by_id(), (id,))).get_first()
    def get_items_by_any_column(self, col_name: str, col_value: any, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), (col_value,)))
    def get_items_by_any_column_values(self, col_name: str, col_values: Iterable, n: int = 1000) -> system_version_read_dtos:
        return system_version_read_dtos(self.get_items_with_params(self.get_model().get_select_active_by_any_column(col_name, n), col_values))
    def get_uids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_keys(n))
    def get_guids(self, n: int = 1000) -> list[str]:
        return self.get_column_values_all(self.get_model().get_select_all_guids(n))
    def get_items_by_system_version_uid(self, col_value: any, n: int = 1000) -> system_version_read_dtos:
        return self.get_items_by_any_column('system_version_uid', col_value, n)
    def get_items_by_version_description(self, col_value: any, n: int = 1000) -> system_version_read_dtos:
        return self.get_items_by_any_column('version_description', col_value, n)
    def insert_dto(self, dto: system_version_write_dto, created_by: str = "system") -> int:
        return self.insert_single(dto, created_by)
    def insert_row(self, system_version_uid: str , version_description: str ) -> int:
        return self.insert_single(system_version_write_dto.new_write(system_version_uid, version_description))
    def insert_row_random_uid(self, version_description: str ) -> int:
        return self.insert_single(system_version_write_dto.new_write_random_uid(version_description))
    def insert_dtos(self, dtos: list[system_version_write_dto], created_by: str = "system") -> int:
        return self.insert_many(dtos, created_by)
    def insert_write_dtos(self, dtos: system_version_write_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.dtos, created_by)
    def insert_read_dtos(self, dtos: system_version_read_dtos, created_by: str = "system") -> int:
        return self.insert_dtos(dtos.get_write_dtos(), created_by)
    def insert_and_get(self, dto: system_version_write_dto, created_by: str = "system") -> system_version_read_dto | None:
        self.insert_single(dto, created_by)
        return self.get_item_by_uid(dto.get_uid())
    def insert_and_get_many(self, dtos: system_version_write_dtos, created_by: str = "system") -> system_version_read_dtos:
        return system_version_read_dtos(list(map(lambda dto: self.insert_and_get(dto, created_by), dtos.dtos)))
    def upsert_row(self, system_version_uid: str , version_description: str , updated_by: str="system") -> int:
        params = system_version_write_dto.new_write(system_version_uid, version_description).get_list_write_insert(updated_by)
        return self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
    def upsert_row_and_get(self, system_version_uid: str , version_description: str , updated_by: str = "system") -> system_version_read_dto | None:
        params = system_version_write_dto.new_write(system_version_uid, version_description).get_list_write_insert(updated_by)
        self.execute_query_with_params(self.get_model().upsert_attrs_sql, params)
        return self.get_item_by_uid(system_version_uid)
    def delete_logical_dtos(self, dtos: list[system_version_write_dto], removed_by: str = "system") -> int:
        uids = list(map(lambda dto: dto.get_uid(), dtos))
        return self.delete_logical_by_uids(uids, removed_by)
    def delete_logical_write_dtos(self, dtos: system_version_write_dtos, removed_by: str = "system") -> int:
        return self.delete_logical_dtos(dtos.dtos, removed_by)

# auto-generated - DaoRead - END

