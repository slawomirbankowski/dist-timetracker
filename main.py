# Main entry point for TimeTracker app
import os
import psycopg2
import psycopg2.pool
from pyliquibase import Pyliquibase

import dao
# import dto
# import service
# import controller

import controller.controllers

from dao import dao_connection
from dto.dtos import account_instance_dto

# from controller import ClientController
# from controller import MainController
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Start')
    daoConn = dao_connection.daoConn
    print('MAIN ::: Got DAO')
    print(daoConn)
    conn = daoConn.getConnection()
    print(conn)
    cursor = conn.cursor()
    cursor.execute("select * from public.account_instance")
    results = cursor.fetchall()
    account_instances = []
    for row in results:
        print(row)
        account_instance = account_instance_dto( *row)
        print(account_instance)
        account_instances.append(account_instance)
    #for ai in account_instances:
    #    print(ai)
    #print(account_instances)

    conn.close()
    #conn2 = daoConn.getConnection()
    #print('MAIN ::: Got connection')
    #print(conn2)
    #conn2.close()
    # initialize Liquibase schema
    #daoConn.initializeSchema()

    ##print(controller.controllers.version)
    #print('Start listening on HTTP port')
    ##controller.controllers.startHttpListening()
