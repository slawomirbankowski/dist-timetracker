import datetime
from abc import abstractmethod
from dataclasses import dataclass
import uuid
import random
from random import randrange, uniform, randint
from typing import Iterable

from base.base_objects import base_object


# base model class to keep objects representing tables in database
@dataclass(frozen=False)
class base_model(base_object):
    table_name: str  # name of table in database
    key_column_name: str  # name of UID column, typically it is table_uid
    all_columns: list[str]  # list od all column names
    attr_columns: list[str]  # list of attribute columns
    insert_columns: list[str]  # list of attribute columns
    insert_columns_list: str  #
    insert_columns_question_marks: str  #
    attr_no_uid_columns: list[str]
    attr_no_uid_columns_eq: list[str]
    all_columns_list: str  # all column comma separated list like id,col1,col2,col3,created_date,...
    attr_columns_list: str  # list of attributes list like col1,col2,col3,...
    attr_no_uid_columns_list: str  # list of attributes list like col1,col2,col3,...
    attr_no_uid_columns_eq_list: str
    all_question_marks: str  # question marks like ?,?,?,?,?
    attr_question_marks: str  #
    insert_attrs_sql: str
    update_attrs_sql: str
    upsert_columns: list[str]
    upsert_columns_exclude_list: str
    upsert_attrs_sql: str
    select_all_sql: str

    def __init__(self, table_name: str, attr_columns: list[str]):
        # only attr_columns should be passed
        super().__init__()
        self.table_name = table_name
        self.key_column_name = self.table_name + "_uid"
        self.all_columns = []
        self.all_columns.append("id")
        for c in attr_columns:
            self.all_columns.append(c)
        self.all_columns.append("row_guid")
        self.all_columns.append("row_version")
        self.all_columns.append("is_active")
        self.all_columns.append("created_date")
        self.all_columns.append("created_by")
        self.all_columns.append("last_updated_date")
        self.all_columns.append("last_updated_by")
        self.all_columns.append("removed_date")
        self.all_columns.append("removed_by")
        self.all_columns.append("custom_attributes")
        self.attr_columns = attr_columns
        self.insert_columns = self.attr_columns.copy()
        self.insert_columns.append("created_by")
        self.insert_columns.append("last_updated_by")
        self.insert_columns.append("custom_attributes")
        self.insert_columns_list = ",".join(self.insert_columns)
        self.insert_columns_question_marks = ",".join(list(map(lambda x: "%s", self.insert_columns)))
        self.attr_no_uid_columns = [x for x in self.attr_columns if x != self.key_column_name]
        self.attr_no_uid_columns_eq = [x+"=%s" for x in self.attr_no_uid_columns]
        self.all_columns_list = ','.join(self.all_columns)
        self.attr_columns_list = ",".join(attr_columns)
        self.attr_no_uid_columns_list = ",".join(self.attr_no_uid_columns)
        self.attr_no_uid_columns_eq_list = ",". join(self.attr_no_uid_columns_eq)
        self.all_question_marks = ",".join(list(map(lambda x: "%s", self.all_columns)))
        self.attr_question_marks = ",".join(list(map(lambda x: "%s", attr_columns)))
        self.insert_attrs_sql = "insert into " + self.table_name + "(" + self.insert_columns_list + ") values (" + self.insert_columns_question_marks + ")"
        self.update_attrs_sql = "update " + self.table_name + " set " + self.attr_no_uid_columns_eq_list + ", custom_attributes=%s, last_updated_date=now(), row_version=row_version+1, last_updated_by=%s where " + self.key_column_name + "=%s"
        self.upsert_columns = self.attr_no_uid_columns.copy()
        self.upsert_columns.append("last_updated_by")
        self.upsert_columns.append("custom_attributes")
        self.upsert_columns_exclude_list = ",".join([x+"=excluded."+x for x in self.upsert_columns])
        self.upsert_attrs_sql = "insert into " + self.table_name + "(" + self.insert_columns_list + ") values (" + self.insert_columns_question_marks + ") on conflict (" + self.table_name + "_uid) do update set " + self.upsert_columns_exclude_list + ", last_updated_date=now()"
        self.select_all_sql = "select * from " + self.table_name
    def get_base_dict_custom_info(self) -> dict[str, any]:
        return {
            "table_name": self.table_name,
            "key_column_name": self.key_column_name,
            "attr_columns": self.attr_columns,
            "insert_columns": self.insert_columns,
            "insert_columns_list": self.insert_columns_list,
            "insert_attrs_sql": self.insert_attrs_sql,
            "update_attrs_sql": self.update_attrs_sql
        }
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Model"
    # get name of base object
    def get_base_object_name(self) -> str:
        return self.table_name
    def get_uid_column_name(self) -> str:
        return self.table_name + "_uid"

    def get_name_column_name(self) -> str:
        return self.table_name + "_uid"

    def get_key_column_name(self) -> str:
        return self.table_name + "_uid"

    def get_insert_sql(self) -> str:
        return self.insert_attrs_sql

    def get_select_all_limit_sql(self, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " limit " + str(max_rows)
    def get_select_active_limit_sql(self, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " where is_active=1 limit " + str(max_rows)
    def get_select_all_latest_sql(self, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " order by created_date desc limit " + str(max_rows)
    def get_select_active_latest_sql(self, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " order by created_date desc limit " + str(max_rows)

    def get_select_write_all_limit_sql(self, max_rows: int = 1000) -> str:
        return "select " + self.attr_columns_list + " from " + self.table_name + " limit " + str(max_rows)
    def get_select_write_active_limit_sql(self, max_rows: int = 1000) -> str:
        return "select " + self.attr_columns_list + " from " + self.table_name + " where is_active=1 limit " + str(max_rows)
    def get_select_write_all_latest_sql(self, max_rows: int = 1000) -> str:
        return "select " + self.attr_columns_list + " from " + self.table_name + " order by created_date desc limit " + str(max_rows)
    def get_select_write_active_latest_sql(self, max_rows: int = 1000) -> str:
        return "select " + self.attr_columns_list + " from " + self.table_name + " order by created_date desc limit " + str(max_rows)
    def get_select_all_uids(self, max_rows: int = 1000) -> str:
        return "select " + self.get_key_column_name() + " from " + self.table_name + " order by " + self.get_key_column_name() + " limit " + str(max_rows)
    def get_select_all_keys(self, max_rows: int = 1000) -> str:
        return "select " + self.get_key_column_name() + " from " + self.table_name + " order by " + self.get_key_column_name() + " limit " + str(max_rows)
    def get_select_all_names(self, max_rows: int = 1000) -> str:
        return "select " + self.get_key_column_name() + " from " + self.table_name + " order by " + self.get_key_column_name() + " limit " + str(max_rows)
    def get_select_all_guids(self, max_rows: int = 1000) -> str:
        return "select row_guid from " + self.table_name + " limit " + str(max_rows)
    def get_select_keys_by_column_name(self, col_name: str, max_rows: int = 1000) -> str:
        return "select " + self.get_key_column_name() + " from " + self.table_name + " where " + col_name + "=%s order by " + self.get_key_column_name() + " limit " + str(max_rows)
    def get_select_guids_by_column_name(self, col_name: str, max_rows: int = 1000) -> str:
        return "select row_guid from " + self.table_name + " where " + col_name + "=%s limit " + str(max_rows)

    def get_select_count_all_sql(self) -> str:
        return "select count(*) as cnt from " + self.table_name
    def get_select_count_active_sql(self) -> str:
        return "select count(*) as cnt from " + self.table_name + " where is_active=1"
    def get_select_count_by_any_column_sql(self, column_name: str) -> str:
        return "select count(*) as cnt from " + self.table_name + " where is_active=1 and " + column_name + "=%s"
    def get_select_count_by_two_columns_sql(self, col1: str, col2: str) -> str:
        return "select count(*) as cnt from " + self.table_name + " where is_active=1 and " + col1 + "=%s and " + col2 + "%s"

    def get_select_by_key(self) -> str:
        return "select * from " + self.table_name + " where " + self.key_column_name + "=%s"
    def get_select_by_id(self) -> str:
        return "select * from " + self.table_name + " where id=%s limit 1"
    def get_select_active_only(self) -> str:
        return "select * from " + self.table_name + " where is_active=1 order by created_date desc limit 1000"
    def get_select_active_by_any_column(self, column_name: str, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " where is_active=1 and " + column_name + "=%s order by created_date desc limit " + str(max_rows)
    def get_select_active_by_any_column_values(self, column_name: str, values: Iterable, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " where is_active=1 and " + column_name + " in (%s) order by created_date desc limit " + str(max_rows)
    def get_select_with_custom_where(self, where_sql: str, max_rows: int = 1000) -> str:
        return "select * from " + self.table_name + " where " + where_sql + " limit " + str(max_rows)


# base DTO with nothing
class base_dto:
    @classmethod
    def get_random_uid(cls) -> str:
        return str(uuid.uuid4())

    @classmethod
    def get_random_uid_for_object(cls, prefix: str, obj: any) -> str:
        return prefix + "_" + type(obj).__name__ + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(uuid.uuid4())[:13].replace("-", "_")

    @classmethod
    def get_random_uid_with_name(cls, prefix: str) -> str:
        return prefix + "_" + str(datetime.datetime.now())[:10].replace("-", "_") + "_" + str(uuid.uuid4())[:13].replace("-", "_")

    @classmethod
    def get_random_int(cls) -> int:
        return random.randint(0, 1000000)
    @classmethod
    def get_random_float(cls) -> float:
        return random.uniform(0, 1000000)
    @classmethod
    def get_random_date(cls) -> int:
        # TODO: generate random date and time
        return str(uuid.uuid4())


# base class for DTO with custom_attributes
class base_custom_dto(base_dto):
    custom_attributes: str
    def get_custom_attributes(self) -> str:
        return self.custom_attributes
    def get_custom_attributes_as_dict(self):
        return None
    def get_custom_attributes_names(self):
        return None

# base DTO to insert/write row into DB
class base_write_dto(base_custom_dto):
    def __init__(self):
        print("Creating new DTO")
    @abstractmethod
    def get_key(self) -> str:
        pass
    @abstractmethod
    def get_uid(self) -> str:
        pass
    @abstractmethod
    def get_model(self) -> base_model:
        pass
    @abstractmethod
    def get_list_values(self) -> list[any]:
        pass
    @abstractmethod
    def get_list_values_no_custom(self) -> list[any]:
        pass
    @abstractmethod
    def get_list_write_update(self, updated_by: str) -> list[any]:
        pass
    @abstractmethod
    def get_list_write_insert(self, created_by: str) -> list[any]:
        pass
    @abstractmethod
    def get_nonkey_values(self) -> list[any]:
        pass
    @abstractmethod
    def get_nonkey_values_with_custom(self) -> list[any]:
        pass
    # get table name for this write DTO class
    def get_table_name(self) -> str:
        return self.get_model().table_name
    @abstractmethod
    def to_write_dict(self) -> dict:
        pass
    @abstractmethod
    def clone_write(self):
        pass
    @abstractmethod
    def clone_write_new_uid(self):
        pass
    @abstractmethod
    def clone_with_uid(self, uid: str):
        pass
    @abstractmethod
    def to_json_write(self) -> str:
        pass
    @abstractmethod
    def update_uid(self, uid: str):
        pass

# base class for DTO classes
class base_read_dto(base_write_dto):
    id: int
    row_guid: str
    row_version: int
    is_active: int
    created_date: datetime.datetime
    created_by: str
    last_updated_date: datetime.datetime
    last_updated_by: str
    removed_date: datetime.datetime | None
    removed_by: str | None
    custom_attributes: str
    def get_id(self) -> int:
        return self.id
    def get_created_date(self) -> datetime.datetime:
        return self.created_date
    def get_last_updated_date(self) -> datetime.datetime:
        return self.last_updated_date
    def is_removed(self) -> bool:
        return self.removed_date is not None
    @abstractmethod
    def to_read_dict(self) -> dict:
        pass
    @abstractmethod
    def to_write(self):
        pass
    @abstractmethod
    def to_thin(self):
        pass
    @abstractmethod
    def touch(self, updated_by: str = "system"):
        pass
    @abstractmethod
    def get_list_all_values(self) -> list[any]:
        pass
    @abstractmethod
    def get_list_update_values(self, updated_by: str) -> list[any]:
        pass
    @abstractmethod
    def is_older_than(self, dt: datetime.datetime) -> bool:
        pass
    @abstractmethod
    def is_newer_than(self, dt: datetime.datetime) -> bool:
        pass
    @abstractmethod
    def to_json_read(self) -> str:
        pass


# helper class to store list of items
class base_dtos:
    dtos: list[base_read_dto]
    def __init__(self, dtos: list[base_read_dto]):
        self.dtos = dtos
    def get_dtos(self) -> list[base_read_dto]:
        return self.dtos
    def get_keys(self) -> list[str]:
        return list(map(lambda dto: dto.get_key(), self.dtos))
    def get_active_dtos(self):
        return list(filter(lambda x: x.is_active == 1, self.dtos))
    # count number of rows in this collection
    def count(self) -> int:
        return len(self.dtos)
    def count_active_only(self):
        return len(self.get_active_dtos())
    def touch_all(self, updated_by: str = "system"):
        for dto in self.dtos:
            dto.touch(updated_by)
    @abstractmethod
    def get_write_dicts(self) -> list[dict]:
        pass
    @abstractmethod
    def get_read_dicts(self) -> list[dict]:
        pass
    @abstractmethod
    def find_by_uid(self, uid: str):
        pass
    @abstractmethod
    def get_first(self):
        pass

@dataclass(frozen=False)
class group_dto:
    value: str
    rows_count: any
