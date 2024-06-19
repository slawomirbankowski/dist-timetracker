import datetime
import json
import logging
from dataclasses import dataclass, asdict
from logging import config
from functools import wraps
from typing import Callable

from flask import Flask, jsonify, request, abort, Request, Response
from base.base_objects import base_object, AccountSessionBase, objects, AccountPermissionsBase, RequestBase, \
    ResponseBase
from base.base_utils import get_random_uid_with_prefix, get_random_uid_long_with_prefix


@dataclass(frozen=False)
class ResponseSessionError:
    code: int
    error: str


# request HTTP
class RequestSession(RequestBase):
    """full HTTP request object with url, headers, cookies, parameters, body"""
    request: Request
    url: str
    controller_name: str
    method_name: str
    request_id: str
    created_date: datetime.datetime
    authorization_header: str
    authorization_method: str
    authorization_token: str
    account_session: AccountSessionBase | None
    account_permission: AccountPermissionsBase | None
    body_as_text: str | None = None
    body_as_dict: dict | None = None

    def __init__(self, request: Request, controller_name: str, method_name: str):
        self.request = request
        #self.request.remote_addr
        self.created_date = datetime.datetime.now()
        self.url = request.url
        self.request_id = get_random_uid_long_with_prefix("REQ")
        self.controller_name = controller_name
        self.method_name = method_name
        if request.authorization is None:
            self.authorization_header = ""
        else:
            self.authorization_header = str(request.authorization)
        auth_tab = self.authorization_header.split(" ")
        if len(auth_tab) > 0:
            self.authorization_method = auth_tab[0]
        else:
            self.authorization_method = "None"
        if len(auth_tab) > 1:
            self.authorization_token = auth_tab[1]
        else:
            self.authorization_token = ""
        logging.info("Creating new HTTP session for request: " + request.full_path +", controller: " + controller_name + ", method: " + method_name)

    def get_method_full_name(self) -> str:
        return self.request.method + ":/" + self.method_name
    def get_content_type(self) -> str:
        if self.request.content_type is None:
            return ""
        else:
            return str(self.request.content_type)
    # returns host with port like: localhost:8000
    def get_host(self) -> str:
        return self.request.host
    # get full URL like http://localhost:8000/api/test?param1=value1&param2=value2&param3=value3
    def get_url(self) -> str:
        return self.request.url
    # get path like: /api/test
    def get_path(self) -> str:
        return self.request.path
    def get_remote_address(self) -> str:
        return str(self.request.remote_addr)
    def get_query_string(self) -> str:
        return str(self.request.query_string)
    def get_query_param(self, name: str, default_value: str = "") -> str:
        if self.request.args.__contains__(name):
            return request.args[name]
        else:
            return default_value
    def get_query_or_body_param(self, name: str, default_value: str = "") -> str:
        if self.request.args.__contains__(name):
            return request.args[name]
        else:
            body_dict = self.get_body_as_dict()
            if body_dict.__contains__(name):
                return body_dict[name]
            return default_value

    def get_query_or_body_param_as_int(self, name: str, default_value: int = "") -> int:
        try:
            value_str = self.get_query_or_body_param(name, str(default_value))
            return int(value_str)
        except:
            return default_value

    def get_query_params(self, name: str, default_list: list[str] = []) -> list[str]:
        if self.request.args.__contains__(name):
            return request.args.getlist(name)
        else:
            return default_list
    def get_body_as_text(self) -> str:
        if self.body_as_text is not None:
            return self.body_as_text
        else:
            self.body_as_text = self.request.data.decode()
            return self.body_as_text
    def get_body_as_dict(self) -> dict:
        try:
            obj = json.loads(self.get_body_as_text())
            if type(obj).__name__ == "dict":
                self.body_as_dict = obj
                return self.body_as_dict
            else:
                return {}
        except:
            return {}
    def get_body_as_json_parsed(self) -> any:
        try:
            x = json.loads(self.get_body_as_text())
            self.body_as_any = x
            return self.body_as_any
        except:
            return {}
    def get_authorization_header(self) -> str:
        return self.authorization_header
    def get_authorization_method(self) -> str:
        return self.authorization_method
    def get_authorization_token(self) -> str:
        return self.authorization_token
    def get_cookie_value(self, name: str, default_value: str = "") -> str:
        if self.request.cookies.__contains__(name):
            return request.cookies[name]
        else:
            return default_value
    def get_cookie_values(self, name: str, default_list: list[str] = []) -> list[str]:
        if self.request.cookies.__contains__(name):
            return request.cookies.getlist(name)
        else:
            return default_list
    def get_header_value(self, name: str, default_value: str = "") -> str:
        if self.request.headers.__contains__(name):
            return request.headers[name]
        else:
            return default_value
    def set_account_session(self, account_session: AccountSessionBase | None):
        self.account_session = account_session
    def set_account_permission(self, account_permission: AccountPermissionsBase | None):
        self.account_permission = account_permission
    def has_roles(self, required_roles: set[str]) -> bool:
        if len(required_roles) == 0:
            return True
        if self.account_permission is None:
            return False
        return not self.account_permission.all_roles.isdisjoint(required_roles)

    def to_myself_dict(self) -> dict:
        return {"account": asdict(self.account_permission.account_dto),
                "tenant": asdict(self.account_permission.tenant_dto.to_thin()),
                "groups": self.account_permission.groups_list,
                "created_date": str(self.account_permission.created_date),
                "roles": list(self.account_permission.roles),
                "all_roles": list(self.account_permission.all_roles),
                "session_load_date": str(self.account_session.session_load_date),
                "permission_load_date": str(self.account_permission.permission_load_date),
                "valid_till_date": str(self.account_session.valid_till_date),
                "session_id": self.account_session.session_id}


class ResponseSession(ResponseBase):
    """full HTTP response"""
    code: int = 200  # full HTTP code of response
    req_session: RequestSession  # connected request session object
    obj: dict[str, any] | None  # object to be returned
    end_time: datetime.datetime | None  # end time of that response
    error_message: str  # test error message

    def __init__(self, req_session: RequestSession, obj: dict[str, any] | None = None, code: int = 200, error_message: str = ""):
        self.req_session = req_session
        self.obj = obj
        self.code = code
        self.error_message = error_message
    def get_final_response(self) -> Response:
        total_time = datetime.datetime.now() - self.req_session.created_date
        logging.info("___________________OBJ TYPE: " + str(type(self.obj).__name__))
        final_obj = {
            "result": self.obj,
            "metadata": {
                "status": "",
                "error_message": self.error_message,
                "request_id": self.req_session.request_id,
                "created_date": str(self.req_session.created_date),
                "system_instance_uid": objects.system_instance_uid,
                "total_time": total_time.total_seconds(),
                "code": self.code
            }
        }
        res = jsonify(final_obj)
        res.status_code = self.code
        return res

    @classmethod
    def ok(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 200)
    @classmethod
    def ok_status(cls, req_session: RequestSession, status_name: str = "OK"):
        return cls(req_session, {"status": status_name}, 200)
    @classmethod
    def ok_object(cls, req_session: RequestSession, obj: any):
        return cls(req_session, asdict(obj), 200)

    @classmethod
    def bad_request(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 400)
    @classmethod
    def unauthorized_request(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 401)
    @classmethod
    def payment_required(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 402)
    @classmethod
    def forbidden(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 403)
    @classmethod
    def not_found(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 404)
    @classmethod
    def internal_server_error(cls, req_session: RequestSession, obj: dict[str, any] = {}):
        return cls(req_session, obj, 500)
    @classmethod
    def not_implemented(cls, req_session: RequestSession):
        return cls(req_session, {"status": "NOT_IMPLEMENTED"}, 501, "This feature is not yet implemented")
    @classmethod
    def any_response(cls, req_session: RequestSession, obj: dict[str, any] = {}, code: int = 200, error: str = ""):
        return cls(req_session, obj, code, error)

    def set_end_time(self):
        self.end_time = datetime.datetime.now()

class BaseController(base_object):
    """base class for controllers to have HTTP endpoints"""
    requests_count: int
    last_use_date = datetime.datetime
    def __init__(self):
        super().__init__()
        self.requests_count = 0
        self.last_use_date = datetime.datetime.now()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Controller"

    def use(self) -> None:
        """"""
        self.requests_count += 1
        self.last_use_date = datetime.datetime.now()

    def info(self, session: RequestSession) -> ResponseSession:
        i = self.get_base_dict_info()
        i.update({
            "requests_count": self.requests_count,
            "last_use_date": str(self.last_use_date)
        })
        return ResponseSession.ok(session, i)


class ControllerRoute(base_object):
    """single route to be executed in controllers - route has key, description and method to be executed; authorization might be required with list of roles"""
    key: str  # key for request like GET:/auth/login
    route_description: str  # friendly description of this route
    controller_method: Callable[[RequestSession], ResponseSession]  # controller method to be run
    require_account: bool  # if that route requires valid token representing an account
    roles: set[str]  # list of high-level roles needed to run this method
    def __init__(self, key: str, route_description: str, controller_method: Callable[[RequestSession], ResponseSession], require_account: bool = False, roles: set[str] = []):
        super().__init__()
        self.key = key
        self.route_description = route_description
        self.controller_method = controller_method
        self.require_account = require_account
        self.roles = roles
    def get_base_object_type(self) -> str:
        return "route"
    # get name of base object
    def get_base_object_name(self) -> str:
        return str(self.key)
    def to_dict(self) -> dict:
        return {
            "key": self.key,
            "route_description": self.route_description,
            "require_account": self.require_account,
            "roles": list(self.roles)
        }