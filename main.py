import os
import logging
import atexit
import dao.dao_connection
from base.base_objects import objects
from base.cache import cache
from dao.daos import daos
from dto.dtos_models import db_models
from service.services import services
from controller.controller_app import start_http_listening
from controller.controllers import controllers


if __name__ == '__main__':
    print("=================================================== STARTING")
    logging.info("Starting new Python application")
    #logging.log(2, "Some log")
    db_url = os.environ.get('JDBC_URL')
    db_host = os.environ.get('JDBC_HOST')
    db_name = os.environ.get('JDBC_NAME')
    db_user = os.environ.get('JDBC_USER')
    db_pass = os.environ.get('JDBC_PASS')
    #logging.basicConfig()
    logging.info("Main database URL =" + db_url)
    logging.info("Main database HOST=" + db_host)
    logging.info("Main database NAME=" + db_name)
    logging.info("Main database USER=" + db_user)
    print("=================================================== OBJECTS")
    objects.initialize()
    print("=================================================== CACHE")
    cache.initialize()
    print("=================================================== MODELS")
    # initialize all models
    db_models.initialize()
    print("=================================================== CONNECTIONS")
    # initialize DB connections
    dao.dao_connection.db_connections.initialize_main_connection(db_url, db_host, db_name, db_user, db_pass)
    print("=================================================== DAS")
    # initialize services
    daos.initialize_daos()
    print("=================================================== SERVICES")
    services.initialize_services()
    print("=================================================== CONTROLLERS")
    controllers.initialize_controllers()
    print("=================================================== HTTP")
    start_http_listening()


def exit_handler():
    print("TimeTracker application is ending")
    controllers.close()
    daos.close()
    dao.dao_connection.db_connections.close()
    db_models.close()
    objects.close()
    print("TimeTracker ENDED!!!")


atexit.register(exit_handler)
