import os
import logging
import atexit
import sys
import logging
from logging import config
import redis
from base.base_constants import SystemVersions
import dao.dao_connection
from base.base_objects import objects
from base.cache import cache
from dao.dao_base import simple_dao
from dao.daos import daos
from dto.dtos_models import db_models
from service.services import services
from controller.controllers_app import start_http_listening
from controller.controllers import controllers


def main_application() -> None:
    logging.info(f"Starting new Python application of version: {SystemVersions.Latest}" )
    logging.info("=================================================== OBJECTS")
    objects.initialize()
    logging.info("=================================================== CACHE")
    cache.initialize()
    logging.info("=================================================== MODELS")
    # initialize all models
    db_models.initialize()
    logging.info("=================================================== CONNECTIONS")
    # initialize DB connections
    dao.dao_connection.db_connections.initialize_main_connection_from_env()
    logging.info("=================================================== DAOs")
    # initialize services
    daos.initialize_daos()
    logging.info("=================================================== SERVICES")
    services.initialize()
    logging.info("=================================================== CONTROLLERS")
    controllers.initialize_controllers()
    logging.info("=================================================== HTTP")
    start_http_listening()


def generate_files() -> None:
    dao.dao_connection.db_connections.initialize_main_connection_from_env()
    rich_views_def = db_models.generate_all_rich_views()
    f = open("./tmp/rich_views.xml.generated", "w")
    f.writelines(rich_views_def)
    f.close()
    python_files_to_generate = daos.dao.get_column_values_by_params("select table_name from v_definition_generate_list")
    for table_name in python_files_to_generate:
        python_file = "./tmp/" + table_name[20:] + ".py.generated"
        rows = daos.dao.get_column_values_by_params(f"select python from {table_name}  order by table_name, ordinal_position")
        print("Generate python file for table: " + table_name + " into python fle: " + python_file)
        f = open(python_file, "w")
        f.writelines([row+"\n" for row in rows])
        f.close()
        daos.dao.create_rich_views()

def rich_views_replace():
    dao.dao_connection.db_connections.initialize_main_connection_from_env()
    daos.dao.replace_rich_views()

def test():
    print("TEST")


if __name__ == '__main__':
    print("START")
    main_application()

    # logging.info("Info log")
    # logging.debug("Debug log log")
    # logging.warning("Warning log log")
    # objects.initialize()
    # cache.initialize()
    # db_models.initialize()
    # db_models.generate_rich_view(db_models.account_instance_model)
    # db_models.print_all_rich_views()
    # conn = dao.dao_connection.db_connections.get_connection()
    #generate_files()
    #dao.dao_connection.db_connections.initialize_main_connection_from_env()
    #daos.dao.replace_rich_views()


    # daos.dao.with_connection_select(lambda wrp: wrp.)
    # print(str(type(conn)))
    # print(str(type(conn).__name__))
    #
    #dao.dao_connection.db_connections.get_connection()
    #row = daos.dao.get_single_row("select * from system_instance limit 1")
    # daos.dao.with_connection_select()
    #print(len(rows))
    #dao.dao_connection.db_connections.read_python_code("select python from v_definition_python_dtos_write")


def exit_handler():
    logging.info("TimeTracker application is ending")
    #controllers.close()
    #daos.close()
    #dao.dao_connection.db_connections.close()
    #db_models.close()
    #objects.close()
    logging.info("TimeTracker ENDED!!!")


atexit.register(exit_handler)
