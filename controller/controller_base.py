import datetime

from flask import Flask, jsonify, request, abort, Request, Response

from base.base_objects import base_object
import json

#
class BaseController(base_object):
    def __init__(self):
        super().__init__()
    # get type of base object
    def get_base_object_type(self) -> str:
        return "Controller"


# request with session - method, parsed user, permissions, ...
class RequestSession:
    request: Request
    method_name: str
    created_date: datetime.datetime = datetime.datetime.now()
    authorization_header: str
    authorization_method: str
    authorization_token: str

    def __init__(self, request: Request, method_name: str):
        self.request = request
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
        print("Creating new HTTP session for request: " + request.full_path)

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
    def get_query_params(self, name: str, default_list: list[str] = []) -> list[str]:
        if self.request.args.__contains__(name):
            return request.args.getlist(name)
        else:
            return default_list
    def get_body_as_text(self) -> str:
        return self.request.data.decode()
    def get_body_as_json_parsed(self) -> any:
        try:
            x = json.loads(self.get_body_as_text())
            return x
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


# full response
class ResponseSession:
    response: Response
    def __init__(self, response: Response):
        self.response = response
    def get_final_response(self):
        return self.response
