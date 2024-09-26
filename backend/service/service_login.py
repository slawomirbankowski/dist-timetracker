import logging
from logging import config
import hashlib
import datetime
from flask import jsonify

from base.base_objects import objects, AccountSessionBase, TokenSaltedHashed
from base.base_utils import get_random_uid, dict_to_json, get_random_uid_very_long_with_prefix
from controller.controller_base import ResponseSession, RequestSession
from dto.dtos import base_dto
from dto.dtos_read import auth_password_read_dto, account_read_dto
from backend.service import service_base, ServiceThreadBase
from backend.dao.daos import daos


class LoginService(ServiceThreadBase):
    token_seq: int
    def __init__(self):
        super().__init__()
        self.token_seq = 0

    # get name of base object
    def get_base_object_name(self) -> str:
        return "LoginService"
    def login(self):
        logging.info("Login")

    def set_password_for_user(self, accinst: account_read_dto, password: str):

        password_salt = base_dto.get_random_uid()
        password_salted = password_salt + password + password_salt
        md5_hash = hashlib.md5()
        md5_hash.update(password_salted.encode())
        password_hash = md5_hash.hexdigest()
        daos.auth_password_dao_instance.set_password(accinst.tenant_uid, accinst.account_uid, password_hash, password_salt)

    def set_password(self, session: RequestSession, account_uid: str, password: str) -> ResponseSession:
        accinst = daos.account_dao_instance.get_account_by_name(account_uid)
        logging.debug("Set password for account: " + account_uid + ", found: " + str(accinst))
        if accinst is not None:
            self.set_password_for_user(accinst, password)
            return ResponseSession.ok(session, {'status': "OK"})
        else:
            return ResponseSession.bad_request(session, {"status": "INCORRECT_ACCOUNT"})

    def change_password(self, session: RequestSession, account_uid: str, current_password: str, new_password: str) -> ResponseSession:
        accinst = daos.account_dao_instance.get_account_by_name(account_uid)
        logging.info(f"Changing current password for account: {account_uid}")
        if accinst is not None:
            if self.check_password_for_account(accinst, current_password):
                self.set_password_for_user(accinst, new_password)
                self.invalidate_session(session.account_session)
                return ResponseSession.ok(session, {"status": "OK"})
            else:
                logging.info(f"Cannot change current password for account: {account_uid}, incorrect current password")
                return ResponseSession.bad_request(session, {"status": "INCORRECT_PASSWORD"})
        else:
            logging.info(f"Changing current password for account: {account_uid}, ")
            return ResponseSession.bad_request(session, {"status": "INCORRECT_ACCOUNT"})

    def request_password(self, session: RequestSession, account_uid: str) -> ResponseSession:
        acc = daos.account_dao_instance.get_account_by_name(account_uid)
        if acc is None:
            logging.info("Request password reset - no account")
        else:
            logging.info(f"Request of password reset for account: {acc.account_uid}")
            reset_guid = get_random_uid_very_long_with_prefix("RESET")
            valid_till_date = datetime.datetime.now() + datetime.timedelta(1.0)  # valid for 1 day (24 hours)
            #daos.email_dao.send(acc.account_email, "Test", f"Reset password for UID: {reset_guid}  VALID_TILL: {str(valid_till_date)}")
            event_notification_uid = None
            daos.auth_request_dao_instance.insert_row(reset_guid, "request_reset_password", acc.tenant_uid, acc.account_uid, acc.account_email, reset_guid, valid_till_date, None, None, None, 0, 0, None, None, event_notification_uid)
        return ResponseSession.ok(session, {"status": "OK"})

    def reset_check(self, session: RequestSession, account_uid: str, reset_guid: str) -> ResponseSession:
        acc = daos.account_dao_instance.get_account_by_name(account_uid)
        req = daos.auth_request_dao_instance.select_row_read_by_uid(reset_guid)
        if acc is not None and req is not None:
            daos.auth_request_dao_instance.update_touch_by_uid(reset_guid)
            daos.auth_request_dao_instance.check(reset_guid)
            return ResponseSession.ok(session, {"status": "EXISTS",
                                                "valid_till_date": str(req.valid_till_date),
                                                "is_active": req.is_active,
                                                "is_used": req.is_used,
                                                "account_uid": req.account_uid,
                                                "account_active": acc.is_active,
                                                "account_type_uid": acc.account_type_uid
                                                })
        else:
            return ResponseSession.not_found(session)

    def reset_password(self, session: RequestSession, account_uid: str, reset_guid: str) -> ResponseSession:
        acc = daos.account_dao_instance.get_account_by_name(account_uid)
        req = daos.auth_request_dao_instance.select_row_read_by_uid(reset_guid)
        if acc is not None and req is not None:
            daos.auth_request_dao_instance.use(reset_guid)
            return ResponseSession.ok(session, {"status": ""})
        else:
            return ResponseSession.not_found(session)

    def check_password_dto(self, dto: auth_password_read_dto, password: str) -> bool:
        nowdt = datetime.datetime.now()
        if dto.date_from < nowdt < dto.date_to:
            password_salted = dto.password_salt + password + dto.password_salt
            md5_hash = hashlib.md5()
            md5_hash.update(password_salted.encode())
            password_hash = md5_hash.hexdigest()
            logging.debug("Check another password for account: " + dto.account_uid + ", salt: " + dto.password_salt + ", hash: " + dto.password_hash + ", produced hash: " + password_hash)
            return password_hash == dto.password_hash
        else:
            return False

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
            # TODO: add auth_attempt ?
            passwords = daos.auth_password_dao_instance.select_rows_read_by_account_uid(accinst.account_uid)
            logging.debug("Found passwords: " + str(len(passwords.dtos)))
            password_ok = passwords.check_any(lambda dto: self.check_password_dto(dto, password))
            if password_ok:
                return ResponseSession.ok(session, {'status': "PASSWORD_OK"})
            else:
                return ResponseSession.bad_request(session, {'status': "PASSWORD_NOT_OK"})

    #
    def token(self, session: RequestSession, grant_type: str, username: str, password: str) -> ResponseSession:
        remote_addr = session.request.remote_addr
        host_name = session.request.host
        cookie_session = session.request.cookies.get("ttsession", None)
        accinst: account_read_dto = daos.account_dao_instance.get_account_by_name(username)
        password_ok = self.check_password_for_account(accinst, password)
        ident_params = dict_to_json({
            "remote_addr": remote_addr,
            "host_name": host_name,
            "cookie_session": cookie_session,
            "grant_type": grant_type,
            "session_created_date": str(session.created_date),
            "session_request_id": session.request_id,
            "password_ok": password_ok
        })
        auth_attempt_uid = "LoginAttempt"+str(session.request_id)
        daos.auth_attempt_dao_instance.insert_row(auth_attempt_uid, auth_attempt_uid, None, None, username, grant_type, ident_params, "REQUESTED")
        if password_ok:
            logging.info("Generating token for account: " + accinst.account_uid + ", grant_type: " + grant_type)
            refresh_token = get_random_uid_very_long_with_prefix("REFRESHTOKEN")
            access_token = get_random_uid_very_long_with_prefix("ACCESSTOKEN")
            id_token = get_random_uid_very_long_with_prefix("IDTOKEN")
            refresh_token_object = TokenSaltedHashed(refresh_token)
            access_token_object = TokenSaltedHashed(access_token)
            id_token_object = TokenSaltedHashed(id_token)
            valid_till_date = datetime.datetime.now() + datetime.timedelta(1.0)
            user_session = objects.create_user_session(accinst.tenant_uid, accinst.account_uid, access_token, access_token_object.token_salt, access_token_object.token_hash, valid_till_date)
            daos.auth_session_dao_instance.insert_row(user_session.session_id, session.request_id, accinst.tenant_uid, accinst.account_uid, id_token, "browser", "desc", host_name)
            logging.debug("Created user session for ID: " + user_session.session_id)
            self.token_seq += 1
            token_sequence_num = self.token_seq
            daos.auth_token_dao_instance.insert_row(access_token, user_session.session_id, auth_attempt_uid, "Access", accinst.tenant_uid, accinst.account_uid, token_sequence_num, access_token_object.token_hash, access_token_object.token_salt, valid_till_date)
            daos.auth_token_dao_instance.insert_row(refresh_token, user_session.session_id, auth_attempt_uid, "Refresh", accinst.tenant_uid, accinst.account_uid, token_sequence_num, refresh_token_object.token_hash, refresh_token_object.token_salt, valid_till_date)
            daos.auth_token_dao_instance.insert_row(id_token, user_session.session_id, auth_attempt_uid, "Id", accinst.tenant_uid, accinst.account_uid, token_sequence_num, id_token_object.token_hash, id_token_object.token_salt, valid_till_date)
            return ResponseSession.ok(session, {"refresh_token": refresh_token, "access_token": access_token, "id_token": id_token, "session_id": user_session.session_id, "valid_till_date": str(valid_till_date)})
        else:
            return ResponseSession.unauthorized_request(session, {"account_uid": username})

    def invalidate_session(self, account_session: AccountSessionBase):
        logging.info(f"Invalidating current session for request: {account_session.session_id}")
        objects.destroy_session(account_session)
        daos.auth_token_dao_instance.delete_logical_by_uid(account_session.token, "")

    def logout(self, session: RequestSession) -> ResponseSession:
        if session.account_session:
            self.invalidate_session(session.account_session)
            #daos.auth_token_dao_instance.delete_logical_by_any_column()
            return ResponseSession.ok(session, {"status": "OK"})
        else:
            return ResponseSession.ok(session, {"status": "NO_ACTIVE_SESSION"})

    def reload_session(self, session: RequestSession) -> ResponseSession:
        if session.account_session:
            objects.destroy_session(session.account_session)
        return ResponseSession.ok(session, session.to_myself_dict())


    def produce_hash(self, session: RequestSession, password: str) -> ResponseSession:
        password_salt = base_dto.get_random_uid()
        password_salted = password_salt + password + password_salt
        md5_hash = hashlib.md5()
        md5_hash.update(password_salted.encode())
        password_hash = md5_hash.hexdigest()
        return ResponseSession.ok(session, {'status': "OK", "password_salt": password_salt, "password_hash": password_hash})


    def produce_passwords_tab(self, session: RequestSession) -> ResponseSession:
        passwords = []
        for i in range(100):
            password = base_dto.get_random_uid()
            password_salt = base_dto.get_random_uid()
            password_salted = password_salt + password + password_salt
            md5_hash = hashlib.md5()
            md5_hash.update(password_salted.encode())
            password_hash = md5_hash.hexdigest()
            single_entry = {"password": password, "password_salt": password_salt, "password_hash": password_hash}
            passwords.append(single_entry)
        return ResponseSession.ok(session, {'status': "OK", "passwords": passwords})


    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True

