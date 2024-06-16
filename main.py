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
from custom.identity_type import *
from custom.identity_type import identity_types
import custom
import smtplib, ssl

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


class MyTestClass:
    def __init__(self):
        print("START CLASS MY TEST CLASS")

def test_email():
        logging.info("Initializing Email DAO")
        port = 587
        smtp_server = "smtp.gmail.com"
        password = "********************"
        sender_email = "disttimetracker@gmail.com"
        to_email = "slawomir.bankowski@gmail.com"
        message = "Request password change form"
        logging.info("Sending email !!!!!!!!!!!!!!!!!!!!!!!!")
        context = ssl.create_default_context()
        # Try to log in to server and send email
        server = None
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo() # Can be omitted
            server.starttls(context=context) # Secure the connection
            server.ehlo() # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, to_email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        finally:
            server.quit()


def test():
    print("TEST")

    #x = globals()[]
    x = type("MyTestClass")
    z = x()

    print(str(type(x)))
    print(str(type(x).__name__))
    print(str(x.__name__))

    print(str(type(z)))
    print(str(type(z).__name__))

    c = globals()["MyTestClass"]
    print(str(type(c)))
    print(str(type(c).__name__))
    cc = c()
    print(str(type(cc)))
    print(str(type(cc).__name__))

    v = eval("MyTestClass()")
    print(str(type(v)))
    print(str(type(v).__name__))

    aa = getattr(custom.identity_type.identity_types, "IdentityTypeOAuth")
    aaa = aa()

    print(str(type(aa)))
    print(str(type(aa).__name__))

    print(str(type(aaa)))
    print(str(type(aaa).__name__))

    #  cache.with_cache("ddd", lambda y: y*1)
    #for k in globals():
    #    logging.info("Key= " + k)


if __name__ == '__main__':
    print("START")
    #generate_files()
    main_application()
    #test_email()

def exit_handler():
    logging.info("TimeTracker application is ending")
    #controllers.close()
    #daos.close()
    #dao.dao_connection.db_connections.close()
    #db_models.close()
    #objects.close()
    logging.info("TimeTracker ENDED!!!")


atexit.register(exit_handler)
