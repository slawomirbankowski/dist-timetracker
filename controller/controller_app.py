from flask import Flask, jsonify, request, abort
from service.services import services
from dao.daos_instances import *
from dao.daos import daos
from controller.controllers import controllers
from controller.controller_base import RequestSession

# main Flask application
httpflaskapp: Flask = Flask(__name__)


#
class FlaskApplicationWrapper(base_object):
    httpflaskapp: Flask
    def __init__(self, httpflaskapp: Flask):
        super().__init__()
        self.httpflaskapp = httpflaskapp
    # get type of base object
    def get_base_object_type(self) -> str:
        return "FlaskApplicationWrapper"
    # get name of base object
    def get_base_object_name(self) -> str:
        return "FlaskApplicationWrapper"


flask_wrapper = FlaskApplicationWrapper(httpflaskapp)


# auth route
@httpflaskapp.route('/api/oauth/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route_oauth(method_name: str):
    return services.with_session(request, method_name, lambda app_req: controllers.auth_controller.route(app_req)).get_final_response()

# route controller method check
@httpflaskapp.route('/api/object/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route_object(method_name: str):
    return services.with_session(request, method_name, lambda app_req: controllers.object_controller.route(app_req)).get_final_response()

# process controller method check
@httpflaskapp.route('/api/process/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route_process(method_name: str):
    return services.with_session(request, method_name,
                          lambda app_req: controllers.process_controller.route(app_req)).get_final_response()

# report controller method check
@httpflaskapp.route('/api/report/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route_report(method_name: str):
    return services.with_session(request, method_name,
                          lambda app_req: controllers.report_controller.route(app_req)).get_final_response()

# report controller method check
@httpflaskapp.route('/api/service/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route_service(method_name: str):
    return services.with_session(request, method_name,
                          lambda app_req: controllers.service_controller.route(app_req)).get_final_response()

# service controller
@httpflaskapp.route('/api/test', methods=['GET'])
def route_test():
    session = RequestSession(request, "")
    print("SESSION get_remote_address: " + session.get_remote_address())
    print("SESSION get_content_type: " + session.get_content_type())
    print("SESSION get_url: " + session.get_url())
    print("SESSION get_path: " + session.get_path())
    print("SESSION get_host: " + session.get_host())
    print("SESSION get_header_value Accept: " + session.get_header_value("Accept"))
    print("SESSION get_header_value Postman-Token: " + session.get_header_value("Postman-Token"))
    print("SESSION get_header_value aaaaaa: " + session.get_header_value("aaaaaa"))
    print("SESSION get_authorization_header: " + session.get_authorization_header())
    print("SESSION get_authorization_method: " + session.get_authorization_method())
    print("SESSION get_authorization_token: " + session.get_authorization_token())
    print("SESSION get_query_param param1: " + session.get_query_param("param1"))
    print("SESSION get_query_param param2: " + session.get_query_param("param2"))
    print("SESSION get_query_param param3: " + session.get_query_param("param3"))
    print("SESSION get_query_params param3: " + ";".join(session.get_query_params("param3")))
    print("SESSION get_query_param param4: " + session.get_query_param("param4"))
    print("SESSION get_cookie_value TOKEN: " + session.get_cookie_value("TOKEN"))
    print("SESSION get_body_as_text: " + session.get_body_as_text())
    print("SESSION get_body_as_json_parsed: " + str(session.get_body_as_json_parsed()))
    print("SESSION get_body_as_json_parsed type: " + str(type(session.get_body_as_json_parsed())))

    print("Run test headers: " + str(type(request.headers)))  # werkzeug.datastructures.headers.EnvironHeaders
    print("Run test headers: " + str(request.headers))
    print("Run test path: " + str(type(request.path)))
    print("Run test path: " + str(request.path))
    print("Run test url: " + str(type(request.url)))
    print("Run test url: " + str(request.url))
    print("Run test base_url: " + str(type(request.base_url)))
    print("Run test base_url: " + str(request.base_url))
    print("Run test cookies: " + str(type(request.cookies))) # werkzeug.datastructures.structures.ImmutableMultiDict
    print("Run test cookies: " + str(request.cookies))
    for c in request.cookies:
        print("Cookie" + c)

    # class 'werkzeug.datastructures.structures.ImmutableMultiDict
    print("Run test content_type: " + str(type(request.content_type)))
    print("Run test content_type: " + str(request.content_type))
    print("Run test host: " + str(type(request.host)))
    print("Run test host: " + str(request.host))
    print("Run test remote_addr: " + str(type(request.remote_addr)))
    print("Run test remote_addr: " + str(request.remote_addr))
    print("Run test authorization: " + str(type(request.authorization)))
    print("Run test authorization: " + str(request.authorization))
    #print("Run test authorization token: " + str(request.authorization.token))

    print("Run test full_path: " + str(type(request.full_path)))
    print("Run test full_path: " + str(request.full_path))

    print("Run test DATA !!!!!!!!!: " + str(request.data))
    print("Run test DATA hex: " + str(request.data.hex()))
    print("Run test DATA decode: " + request.data.decode())


    print("Run test query_string: " + str(type(request.query_string)))
    print("Run test query_string: " + str(request.query_string))

    print("Run test args: " + str(type(request.args)))
    print("Run test args: " + str(request.args))
    for n in request.args.to_dict():
        print("Run test arg type... " + str(type(n)))
        print("Run test arg name: " + str(n))
        print("Run test arg value: " + str(request.args[n]))
    param1 = request.args["param1"]
    print("=========param1: " + str(param1))
    param2 = request.args["param2"]
    print("=========param2: " + str(param2))
    if request.args.__contains__("param3"):
        print("param3=" + request.args["param3"])
    else:
        print("No param 3")

    return jsonify({'user': ""})

# start HTTP interface
def start_http_listening():
    print("Start listening on HTTP 8000")
    httpflaskapp.run(debug=True, port=8000)
    print("End listening")
