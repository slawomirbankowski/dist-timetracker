import os
import datetime
import logging
from pyliquibase import Pyliquibase
import psycopg2
import psycopg2.pool
import dao.dao_connection
from dao.daos import base_dao
from dao.daos import daos
from dao.daos_read import account_division_dao
from dto.dtos_read_list import account_division_read_dtos
from dto.dtos_models import db_models
from dto.dtos_read import account_division_read_dto
from dto.dtos_write import account_division_write_dto
from service.services import services
from controller.controller_app import start_http_listening
from controller.controllers import controllers


def test_model_sqls():
    print('Start')

    print(db_models.account_division_model.get_select_all_limit_sql())
    print(db_models.account_division_model.get_key_column_name())
    print(db_models.account_division_model.get_select_all_latest_sql())
    print(db_models.account_division_model.get_select_all_keys())
    print(db_models.account_division_model.get_select_all_keys(500))
    print(db_models.account_division_model.get_select_count_all_sql())
    print(db_models.account_division_model.get_select_count_active_sql())

def test_cmp():
    print('Start')

    d1 = ["abc", "123", 333]
    d2 = ["abc", "123", 333]
    d3 = ["abc", "1234", 333]
    if d1==d2:
        print("OK")
    if (d1 == d3):
        print("NOT OK")

def test_write_dtos():
    print('Start')

    adw = account_division_write_dto.default_write()
    print(adw)
    print(adw.to_json())

    adr1 = account_division_read_dto.random_read()
    adr2 = account_division_read_dto.random_read()
    adr3 = account_division_read_dto(0, "non-active", "", "", "", 0, 0, datetime.datetime.now(), "system", datetime.datetime.now(), "system", None, None, "{}")

    adlist = account_division_read_dtos([adr1, adr2, adr3])
    print(adlist.dtos)
    adlist.touch_all("me")
    print("adlist.dtos")
    print(adlist.dtos)
    print("adlist.get_keys()")
    print(adlist.get_keys())
    print("adlist.get_active()")
    print(adlist.get_active())
    print("adlist.find_by_uid()")
    print(adlist.find_by_uid(adr1.account_division_uid))
    print(adlist.find_by_uid("not_existing"))
    adlist.get_dtos()
    #account_division_read_dto("", "", "")
    #print(account_division_model.get_select_all_keys())
    #ad = account_division_write_dto("uid", "name", "str")
    #print(ad)

def test_conn():
    db_url = "jdbc:postgresql://localhost:5432/disttimetracker"
    db_user = "postgres"
    db_pass = "************"
    db_pool = psycopg2.pool.SimpleConnectionPool(
        2, 4, user=db_user, password=db_pass,
        host='localhost', port='5432', database='disttimetracker')
    conn = db_pool.getconn()
    print(conn)
    conn.close()
    #liquibase = Pyliquibase(defaultsFile="./changelogs/liquibase.properties", jdbcDriversDir="./lib")
    #print(type(liquibase))
    #print(liquibase.version)
    #liquibase.validate()
    #liquibase.update()

def test_liquibase():
    liquibase = Pyliquibase(defaultsFile="./changelogs/liquibase.properties", jdbcDriversDir="./lib")
    print(type(liquibase))
    print(liquibase.version)
    liquibase.validate()
    liquibase.update()

def test_daoconnection():
    dc = dao.dao_connection.daoConn
    print("try to connect")
    conn = dc.getConnection()
    print(conn)
    conn.close()

def test_basedao():
    dao = base_dao()
    #dtos = dao.get_objects("select * from account_division")
    dtos = dao.get_objects("select * from account_title where id=%s and is_active=%s and account_title_uid=%s", (3,1, "CIO"))
    for dto in dtos:
        print(type(dto))
        print(dto)
    vals = dao.get_column_values_all("select account_title_uid from account_title where id=%s and is_active=%s and account_title_uid=%s", (3,1, "CIO"))
    for dto in vals:
        print(type(dto))
        print(dto)
    row = dao.get_single_row("select * from account_title where id=1")
    print("row")
    print(type(row))
    print(row)
    col_values = dao.get_column_values_all("select account_title_uid from account_title", 0)
    print("col_values")
    print(type(col_values))
    print(col_values)
    value = dao.get_single_value("select account_title_uid from account_title where id=1")
    print("value")
    print(type(value))
    print(value)
    cnt = dao.get_single_value_int_or_default("select count(*) from account_title")
    print("cnt")
    print(type(cnt))
    print(cnt)

def test_base_dao_update():
    print("test update and delete")
    dao = base_dao()
    name = "Test Account"
    uid = "test"
    res = dao.execute_query("update account_instance set display_name=%s where account_instance_uid=%s", (name, uid))
    print(type(res))
    print(res)


def test_customdao():
    cdao = account_division_dao()
    print(cdao)
    dtos = cdao.get_items_all()
    for dto in dtos.dtos:
        print(type(dto))
        print(dto)
        print(dto.to_write())
        print(dto.to_write_dict())
    cnt = cdao.count_all()
    print("cnt")
    print(cnt)
    cnt = cdao.count_active()
    print("cntactive")
    print(cnt)
    print("get_items_by_any_column")
    its = cdao.get_items_by_any_column("division_name", "Default")
    for dto in its.dtos:
        print(type(dto))
        print(dto)
        print(dto.to_write())
        print(dto.to_write_dict())

    cdao.insert()
    acdiv1 = cdao.get_item_by_uid("Default")
    acdiv1.division_description = "new division description"

def test_customdao_insert():
    cdao = account_division_dao()
    ad1 = account_division_write_dto.random_write()
    print(ad1)
    #cdao.insert_single(ad1)
    ads = []
    ads.append(account_division_write_dto.random_write())
    ads.append(account_division_write_dto.random_write())
    ads.append(account_division_write_dto.random_write())
    #cdao.insert_many(ads)
    #cdao.delete_logical_by_uid("bbb2f039-1c93-464a-9e2a-cb2ae9fd53b0", "me")
   # cdao.update_single_column_by_uid("29b627a1-9dd3-40ec-b561-7cfb2b9b6cda", "division_description", "NEW DIVISION")
   # cdao.update_single_column_by_id(3, "division_description", "aaaaaaaa")

    dto = cdao.get_item_by_uid("2036ef7d-4caa-4341-9139-2cdefdfec9b5")
    print(dto)
    dto.division_description="new_desc3333"
    dto.division_name="new_name3333"
    #wdto = dto.to_write()
    #cdao.update_write_dto(dto, "you")
    cdao.upsert_write_dto(dto, "someone")

    ad2 = account_division_write_dto.random_write()
    cdao.upsert_write_dto(ad2, "anyone")


def test_model():
    print(db_models.account_division_model.table_name)
    print(db_models.account_division_model.key_column_name)
    print(db_models.account_division_model.all_columns)
    print("attr_columns")
    print(db_models.account_division_model.attr_columns)
    print("all_columns_list")
    print(db_models.account_division_model.all_columns_list)
    print("attr_columns_list")
    print(db_models.account_division_model.attr_columns_list)
    print("attr_no_uid_columns")
    print(db_models.account_division_model.attr_no_uid_columns)
    print("attr_no_uid_columns_list")
    print(db_models.account_division_model.attr_no_uid_columns_list)
    print("all_question_marks")
    print(db_models.account_division_model.all_question_marks)
    print("attr_question_marks")
    print(db_models.account_division_model.attr_question_marks)
    print("insert_attrs_sql")
    print(db_models.account_division_model.insert_attrs_sql)
    print("update_attrs_sql")
    print(db_models.account_division_model.update_attrs_sql)
    print("upsert_columns")
    print(db_models.account_division_model.upsert_columns)
    print("upsert_columns_exclude_list")
    print(db_models.account_division_model.upsert_columns_exclude_list)
    print("upsert_attrs_sql")
    print(db_models.account_division_model.upsert_attrs_sql)


def testSomething():
    print("Starting new Python application")
    #logging.log(2, "Some log")
    db_url = os.environ.get('JDBC_URL')
    db_host = os.environ.get('JDBC_HOST')
    db_name = "timetracker"  # os.environ.get('JDBC_NAME')
    db_user = "timetracker"  # os.environ.get('JDBC_USER')
    db_pass = "****************"  # os.environ.get('JDBC_PASS')
    print("Main database URL =" + db_url)
    print("Main database HOST=" + db_host)
    print("Main database NAME=" + db_name)
    print("Main database USER=" + db_user)
    print("Main database PASS=" + db_pass)
    # initialize all models
    db_models.initialize()
    # initialize DB connections
    dao.dao_connection.db_connections.initialize_main_connection(db_url, db_host, db_name, db_user, db_pass)
    # initialize services
    daos.initialize_daos()
    services.initialize_services()
    controllers.initialize_controllers()
    start_http_listening()

if __name__ == '__main__':
    print("======================================= TEST")