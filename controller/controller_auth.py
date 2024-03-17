import datetime

from flask import Flask, jsonify, abort, Request, Response
from dao.daos import daos
from dto.dtos import base_dto
from service.services import services
from controller.controller_base import RequestSession, ResponseSession, BaseController
import hashlib

# Auth controller
class AuthController(BaseController):
    #
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "AuthController"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "AuthController"

    def get_auth_method(self, session: RequestSession) -> ResponseSession:
        account_instance_uid = ""
        daos.account_instance_dao_instance.get_item_by_uid(account_instance_uid)
        return ResponseSession(jsonify({'access_token': "abc123"}))

    def token(self, session: RequestSession) -> ResponseSession:
        # session.request.data
        print("Token request")
        session.get_query_param("grant_type")
        session.get_query_param("username")
        session.get_query_param("password")
        grant_type = session.request.args.getlist("grant_type")
        account_instance_uid = "system"
        accinst = daos.account_instance_dao_instance.get_items_by_account_instance_uid(account_instance_uid)

        accinst.dtos

        if daos.auth_password_dao_instance.check_password("", ""):
            print("Authenticated")
        else:
            print("Not Autenticated")

        return ResponseSession(jsonify({'access_token': "abc123"}))

    def set_password(self, session: RequestSession) -> ResponseSession:
        # session.request.data
        account_instance_uid = session.get_query_param("username")
        password = session.get_query_param("password")
        password_salt = base_dto.get_random_uid()
        password_salted = password_salt + password + password_salt
        md5_hash = hashlib.md5()
        md5_hash.update(password_salted.encode())
        password_hash = md5_hash.hexdigest()
        date_to = datetime.datetime.now() + datetime.timedelta(days=30)
        daos.auth_password_dao_instance.insert_row_random_uid(account_instance_uid, daos.system_instance_dto.system_instance_uid, password_hash, password_salt, datetime.datetime.now(), date_to, 0)
        return ResponseSession(jsonify({'status': "OK"}))

    def check_password(self, session: RequestSession) -> ResponseSession:
        # session.request.data
        #daos.auth_password_dao_instance.get_items_by_any_column("")
       # daos.auth_password_dao_instance.get_items_by_any_column("")
        account_instance_uid = session.get_query_param("username")
        password = session.get_query_param("password")

        accinst = daos.account_instance_dao_instance.get_account_by_name(account_instance_uid)
        if accinst is None:
            return ResponseSession(jsonify({'status': "INCORRECT_PASSWORD"}))
        else:
            passwords = daos.auth_password_dao_instance.get_items_by_account_instance_uid(accinst.account_instance_uid)
            passwords.for_each()

            password_salt = base_dto.get_random_uid()
            password_salted = password_salt + password + password_salt

            md5_hash = hashlib.md5()
            md5_hash.update(password_salted.encode())
            password_hash = md5_hash.hexdigest()
            password_ok = daos.auth_password_dao_instance.check_password(account_instance_uid, password_hash)
            if password_ok:
                return ResponseSession(jsonify({'status': "OK"}))
            else:
                return ResponseSession(jsonify({'status': "INCORRECT_PASSWORD"}))
    def auth(self, session: RequestSession) -> ResponseSession:
        print("Auth")
        return ResponseSession(jsonify({'access_token': "abc123"}))

    def login(self, session: RequestSession) -> ResponseSession:
        print("Auth")
        return ResponseSession(jsonify({'access_token': "abc123"}))

    def myself(self, session: RequestSession) -> ResponseSession:
        print("Auth")
        return ResponseSession(jsonify({'access_token': "abc123"}))

    routes = {
        "set_password": set_password,
        "token": token,
        "auth": auth,
        "login": login,
        "myself": myself
    }

    def route(self, session: RequestSession) -> ResponseSession:
        #session.request.method
        print("Route OAuth with URL: " + session.request.url)
        contr_method = self.routes.get(session.method_name)
        print("Found method" + str(type(contr_method)))
        if contr_method is not None:
            print("Found method")
            return contr_method(self, session)
        else:
            return ResponseSession(abort(404))
