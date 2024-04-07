import os
import logging
import atexit
import sys
import logging
from logging import config
import redis
import dao.dao_connection
from base.base_objects import objects
from base.cache import cache
from dao.daos import daos
from dto.dtos_models import db_models
from service.services import services
from controller.controller_app import start_http_listening
from controller.controllers import controllers

logging.config.fileConfig('logging.conf')


def main_application():
    logging.info("Starting new Python application")
    db_url = os.environ.get('JDBC_URL')
    db_host = os.environ.get('JDBC_HOST')
    db_name = os.environ.get('JDBC_NAME')
    db_user = os.environ.get('JDBC_USER')
    db_pass = os.environ.get('JDBC_PASS')
    logging.info(f"Main database URL ={db_url}, HOST={db_host}, NAME={db_name}, USER={db_user}" )
    logging.info("=================================================== OBJECTS")
    objects.initialize()
    logging.info("=================================================== CACHE")
    cache.initialize()
    logging.info("=================================================== MODELS")
    # initialize all models
    db_models.initialize()
    logging.info("=================================================== CONNECTIONS")
    # initialize DB connections
    dao.dao_connection.db_connections.initialize_main_connection(db_url, db_host, db_name, db_user, db_pass)
    logging.info("=================================================== DAOs")
    # initialize services
    daos.initialize_daos()
    logging.info("=================================================== SERVICES")
    services.initialize_services()
    logging.info("=================================================== CONTROLLERS")
    controllers.initialize_controllers()
    logging.info("=================================================== HTTP")
    start_http_listening()


if __name__ == '__main__':
    main_application()
    #logging.info("Info log")
    #logging.debug("Debug log log")
    #logging.warning("Warning log log")
    #objects.initialize()
    #cache.initialize()
    #db_models.initialize()
    #db_models.generate_rich_view(db_models.account_instance_model)
    #db_models.print_all_rich_views()


def exit_handler():
    logging.info("TimeTracker application is ending")
    #controllers.close()
    #daos.close()
    #dao.dao_connection.db_connections.close()
    #db_models.close()
    #objects.close()
    logging.info("TimeTracker ENDED!!!")


atexit.register(exit_handler)
