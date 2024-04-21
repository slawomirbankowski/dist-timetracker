import logging
from logging import config
import hashlib
import datetime
from flask import jsonify

from base.base_objects import objects
from base.base_utils import get_random_uid
from controller.controller_base import ResponseSession, RequestSession
from dto.dtos import base_dto
from dto.dtos_read import auth_password_read_dto, account_read_dto
from service.services_base import service_base, service_thread_base
from dao.daos import daos


class LoginService(service_thread_base):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "LoginService"
    def login(self):
        logging.info("Login")

    def set_password(self, session: RequestSession, account_uid: str, password: str) -> ResponseSession:
        accinst = daos.account_dao_instance.get_account_by_name(account_uid)
        logging.debug("Set password for account: " + account_uid + ", found: " + str(accinst))
        if accinst is not None:
            password_salt = base_dto.get_random_uid()
            password_salted = password_salt + password + password_salt
            md5_hash = hashlib.md5()
            md5_hash.update(password_salted.encode())
            password_hash = md5_hash.hexdigest()
            daos.auth_password_dao_instance.set_password(accinst.tenant_uid, account_uid, password_hash, password_salt)
            return ResponseSession.ok(session, {'status': "OK"})
        else:
            return ResponseSession.bad_request(session, {"status": "INCORRECT_ACCOUNT"})

    def request_reset_password(self, session: RequestSession, account_uid: str) -> ResponseSession:
        acc = daos.account_dao_instance.get_account_by_name(account_uid)
        if acc is None:
            return ResponseSession.not_implemented(session)
        else:
            daos.auth_request_dao_instance.insert_row("", "name", "tenant", "account", "requestor", "reset", None, "", "", None)
            return ResponseSession.not_implemented(session)

    def check_password_dto(self, dto: auth_password_read_dto, password: str) -> bool:
        password_salted = dto.password_salt + password + dto.password_salt
        md5_hash = hashlib.md5()
        md5_hash.update(password_salted.encode())
        password_hash = md5_hash.hexdigest()
        logging.debug("Check another password for account: " + dto.account_uid + ", salt: " + dto.password_salt + ", hash: " + dto.password_hash + ", produced hash: " + password_hash)
        return password_hash == dto.password_hash

    def check_password_for_account(self, accinst: account_read_dto | None, password: str) -> bool:
        if accinst is None:
            return False
        else:
            passwords = daos.auth_password_dao_instance.select_rows_read_by_account_uid(accinst.account_uid)
            logging.info("Checking passwords for account: " + accinst.account_uid + ", count: " + str(passwords.count()))
            password_ok = passwords.check_any(lambda dto: self.check_password_dto(dto, password))
            return password_ok

    def check_password(self, session: RequestSession, account_uid: str, password: str) -> ResponseSession:
        accinst = daos.account_dao_instance.get_account_by_name(account_uid)
        if accinst is None:
            return ResponseSession.not_found(session, {"account_uid": account_uid})
        else:
            passwords = daos.auth_password_dao_instance.select_rows_read_by_account_uid(accinst.account_uid)
            logging.debug("Found passwords: " + str(len(passwords.dtos)))
            password_ok = passwords.check_any(lambda dto: self.check_password_dto(dto, password))
            if password_ok:
                return ResponseSession.ok(session, {'status': "PASSWORD_OK"})
            else:
                return ResponseSession.bad_request(session, {'status': "PASSWORD_NOT_OK"})

    #
    def token(self, session: RequestSession, grant_type: str, username: str, password: str) -> ResponseSession:
        accinst: account_read_dto = daos.account_dao_instance.get_account_by_name(username)
        password_ok = self.check_password_for_account(accinst, password)
        if password_ok:
            logging.info("Generating token for account: " + accinst.account_uid + ", grant_type: " + grant_type)
            token = get_random_uid()
            token_salt = get_random_uid()
            token_salted = token_salt + token + token_salt
            md5_hash = hashlib.md5()
            md5_hash.update(token_salted.encode())
            token_hash = md5_hash.hexdigest()
            valid_till_date = datetime.datetime.now() + datetime.timedelta(1.0)
            remote_addr = session.request.remote_addr
            host_name = session.request.host
            cookie_session = session.request.cookies.get("ttsession", None)

            user_session = objects.create_user_session(accinst.tenant_uid, accinst.account_uid, token, token_salt, token_hash, valid_till_date)
            logging.debug("Created user session for ID: " + user_session.session_id)
            daos.auth_token_dao_instance.insert_row(token, user_session.session_id, accinst.tenant_uid, accinst.account_uid, 100, token_hash, token_salt, valid_till_date, None, 1)
            return ResponseSession.ok(session, {"token": token, "session_id": user_session.session_id, "valid_till_date": str(valid_till_date)})
        else:
            return ResponseSession.unauthorized_request(session, {"account_uid": username})


    def produce_hash(self, session: RequestSession, password: str) -> ResponseSession:
        password_salt = base_dto.get_random_uid()
        password_salted = password_salt + password + password_salt
        md5_hash = hashlib.md5()
        md5_hash.update(password_salted.encode())
        password_hash = md5_hash.hexdigest()
        return ResponseSession.ok(session, {'status': "OK", "password_salt": password_salt, "password_hash": password_hash})

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True

