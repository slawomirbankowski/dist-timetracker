import datetime
import json
import logging
from logging import config
from flask import Flask, jsonify, abort, Request, Response
from backend.dao.daos import daos
from dto.dtos import base_dto
from backend.service import services
from controller.controller_base import RequestSession, ResponseSession, BaseController
import hashlib


# Test controller
class TestController(BaseController):
    #
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_type(self) -> str:
        return "TestController"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "TestController"

    def info(self, session: RequestSession) -> ResponseSession:
        return ResponseSession.not_implemented(session)

    def test(self, session: RequestSession) -> ResponseSession:
        request = session.request
        logging.info("SESSION get_remote_address: " + session.get_remote_address())
        logging.info("SESSION get_content_type: " + session.get_content_type())
        logging.info("SESSION get_url: " + session.get_url())
        logging.info("SESSION get_path: " + session.get_path())
        logging.info("SESSION get_host: " + session.get_host())
        logging.info("SESSION get_header_value Accept: " + session.get_header_value("Accept"))
        logging.info("SESSION get_header_value Postman-Token: " + session.get_header_value("Postman-Token"))
        logging.info("SESSION get_header_value aaaaaa: " + session.get_header_value("aaaaaa"))
        logging.info("SESSION get_authorization_header: " + session.get_authorization_header())
        logging.info("SESSION get_authorization_method: " + session.get_authorization_method())
        logging.info("SESSION get_authorization_token: " + session.get_authorization_token())
        logging.info("SESSION get_query_param param1: " + session.get_query_param("param1"))
        logging.info("SESSION get_query_param param2: " + session.get_query_param("param2"))
        logging.info("SESSION get_query_param param3: " + session.get_query_param("param3"))
        logging.info("SESSION get_query_params param3: " + ";".join(session.get_query_params("param3")))
        logging.info("SESSION get_query_param param4: " + session.get_query_param("param4"))
        logging.info("SESSION get_cookie_value TOKEN: " + session.get_cookie_value("TOKEN"))
        logging.info("SESSION get_body_as_text: " + session.get_body_as_text())
        logging.info("SESSION get_body_as_json_parsed: " + str(session.get_body_as_json_parsed()))
        logging.info("SESSION get_body_as_json_parsed type: " + str(type(session.get_body_as_json_parsed())))

        logging.info(
            "Run test headers: " + str(type(request.headers)))  # werkzeug.datastructures.headers.EnvironHeaders
        logging.info("Run test headers: " + str(request.headers))
        logging.info("Run test path: " + str(type(request.path)))
        logging.info("Run test path: " + str(request.path))
        logging.info("Run test url: " + str(type(request.url)))
        logging.info("Run test url: " + str(request.url))
        logging.info("Run test base_url: " + str(type(request.base_url)))
        logging.info("Run test base_url: " + str(request.base_url))
        logging.info(
            "Run test cookies: " + str(type(request.cookies)))  # werkzeug.datastructures.structures.ImmutableMultiDict
        logging.info("Run test cookies: " + str(request.cookies))
        for c in request.cookies:
            logging.info("Cookie" + c)

        # class 'werkzeug.datastructures.structures.ImmutableMultiDict
        logging.info("Run test content_type: " + str(type(request.content_type)))
        logging.info("Run test content_type: " + str(request.content_type))
        logging.info("Run test host: " + str(type(request.host)))
        logging.info("Run test host: " + str(request.host))
        logging.info("Run test remote_addr: " + str(type(request.remote_addr)))
        logging.info("Run test remote_addr: " + str(request.remote_addr))
        logging.info("Run test authorization: " + str(type(request.authorization)))
        logging.info("Run test authorization: " + str(request.authorization))
        # logging.info("Run test authorization token: " + str(request.authorization.token))

        logging.info("Run test full_path: " + str(type(request.full_path)))
        logging.info("Run test full_path: " + str(request.full_path))

        logging.info("Run test DATA !!!!!!!!!: " + str(request.data))
        logging.info("Run test DATA hex: " + str(request.data.hex()))
        logging.info("Run test DATA decode: " + request.data.decode())

        logging.info("Run test query_string: " + str(type(request.query_string)))
        logging.info("Run test query_string: " + str(request.query_string))

        logging.info("Run test args: " + str(type(request.args)))
        logging.info("Run test args: " + str(request.args))
        for n in request.args.to_dict():
            logging.info("Run test arg type... " + str(type(n)))
            logging.info("Run test arg name: " + str(n))
            logging.info("Run test arg value: " + str(request.args[n]))
        param1 = request.args["param1"]
        logging.info("=========param1: " + str(param1))
        param2 = request.args["param2"]
        logging.info("=========param2: " + str(param2))
        if request.args.__contains__("param3"):
            logging.info("param3=" + request.args["param3"])
        else:
            logging.info("No param 3")

        return jsonify({'user': ""})
