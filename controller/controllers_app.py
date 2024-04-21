from __future__ import annotations

from datetime import timedelta

from flask import Flask, jsonify, request, abort, Request, Response
import logging
from logging import config
import base.base_objects
from base.base_constants import application_start_date
from service.services import services
from dao.daos_instances import *
from dao.daos import daos
from controller.controllers import controllers
from controller.controller_base import RequestSession, ControllerRoute, ResponseSession

# main Flask application
httpflaskapp: Flask = base.base_objects.httpflaskapp

# all routes - map by key
routes: dict[str, ControllerRoute] = {}


# HTTP endpoint that is listing all endpoints
def endpoints(session: RequestSession) -> ResponseSession:
    routes_info = list(map(lambda key: routes[key].to_dict(), routes))
    return ResponseSession.ok(session, { "endpoints": routes_info})


# all routes - list of available routes
routes_list: list[ControllerRoute] = [
    # service routes
    ControllerRoute("GET:/service/ping", "Just ping to check", controllers.service_controller.ping),
    ControllerRoute("GET:/service/version", "Check version of current application", controllers.service_controller.version),
    ControllerRoute("GET:/service/dao", "Get DAO", controllers.service_controller.dao, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/service/connections", "", controllers.service_controller.connections, True),
    ControllerRoute("GET:/service/objects", "", controllers.service_controller.objs, True),
    ControllerRoute("GET:/service/models", "List models", controllers.service_controller.models, True),
    ControllerRoute("GET:/service/endpoints", "List of HTTP endpoints", endpoints, True),
    ControllerRoute("GET:/service/threads", "Threads", controllers.service_controller.threads, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/service/caches", "", controllers.service_controller.caches, True),
    ControllerRoute("GET:/service/settings", "", controllers.service_controller.settings),
    ControllerRoute("GET:/service/settings-system", "", controllers.service_controller.settings),

    # object routes
    ControllerRoute("GET:/object/info", "", controllers.object_controller.info, True),
    ControllerRoute("GET:/object/count", "", controllers.object_controller.get_object_count, True),
    ControllerRoute("GET:/object/get_list", "", controllers.object_controller.get_objects_list, True),
    ControllerRoute("GET:/object/get_by_uid", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("GET:/object/get_rich_by_uid", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("GET:/object/search", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("POST:/object/create", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("PATCH:/object/update", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("PATCH:/object/check", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("DELETE:/object/delete", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("DELETE:/object/deactivate", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("POST:/object/action", "Run defined action for object", controllers.object_controller.get_object_by_uid, True),

    # account routes
    ControllerRoute("PUT:/account/create", "", controllers.account_controller.create_account, True),
    ControllerRoute("DELETE:/account/deactivate", "", controllers.account_controller.create_account, True),
    ControllerRoute("GET:/account/list", "", controllers.account_controller.list_accounts, True),
    ControllerRoute("GET:/account/get_account_by_uid", "", controllers.account_controller.list_accounts, True),

    # authentication routes
    ControllerRoute("GET:/auth/get_auth_method", "Get authentication method by account name or email or UID", controllers.auth_controller.get_auth_method),
    ControllerRoute("GET:/auth/set_password", "Set password for any user", controllers.auth_controller.set_password, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/auth/my_set_password", "Set password for currently logged user", controllers.auth_controller.my_set_password, True),
    ControllerRoute("GET:/auth/check_password", "", controllers.auth_controller.check_password, True),
    ControllerRoute("GET:/auth/produce_hash", "", controllers.auth_controller.produce_hash),
    ControllerRoute("GET:/auth/token", "Create token with authentication method", controllers.auth_controller.token),
    ControllerRoute("POST:/auth/token", "Create token with authentication method", controllers.auth_controller.token),
    ControllerRoute("GET:/auth/myself", "", controllers.auth_controller.myself, True),
    ControllerRoute("GET:/auth/userinfo", "", controllers.auth_controller.userinfo, True),

    # client routes
    ControllerRoute("POST:/client/info", "", controllers.client_controller.info, True),
    # ControllerRoute("GET:/client/list", "", controllers.client_controller.list_clients, True),

    # competency routes
    # ControllerRoute("POST:/competency/info", "", controllers.competency_controller.info, True),
    # ControllerRoute("GET:/competency/list", "", controllers.competency_controller.list_connections(), True),

    # connection routes
    ControllerRoute("POST:/connection/info", "", controllers.connection_controller.info, True),
    # ControllerRoute("GET:/connection/list", "", controllers.connection_controller.list_connections, True),

    # event routes
    ControllerRoute("POST:/event/info", "", controllers.event_controller.info, True),
    # ControllerRoute("GET:/event/list", "", controllers.event_controller.list_events, True),

    # invoice routes
    ControllerRoute("POST:/invoice/info", "", controllers.invoice_controller.info, True),
    #ControllerRoute("GET:/invoice/list", "", controllers.invoice_controller.list_tenants, True),

    # monitor routes
    ControllerRoute("POST:/monitor/info", "", controllers.monitor_controller.info, True),
    #ControllerRoute("GET:/monitor/list", "", controllers.monitor_controller.list_tenants, True),

    # process routes
    ControllerRoute("POST:/process/info", "", controllers.process_controller.info, True),
    # ControllerRoute("GET:/process/list", "", controllers.process_controller.list_tenants, True),

    # project routes
    ControllerRoute("POST:/project/info", "", controllers.project_controller.info, True),
    # ControllerRoute("GET:/project/list", "", controllers.project_controller.list_tenants, True),

    # report routes
    ControllerRoute("POST:/report/info", "", controllers.report_controller.info, True),
    # ControllerRoute("GET:/report/list", "", controllers.report_controller.list_tenants, True),

    # storage routes
    ControllerRoute("POST:/storage/info", "", controllers.storage_controller.info, True),
    # ControllerRoute("GET:/storage/list", "", controllers.storage_controller.list_tenants, True),

    # synchronization routes
    ControllerRoute("POST:/synchronization/info", "", controllers.synchronization_controller.info, True),
    # ControllerRoute("GET:/synchronization/list", "", controllers.synchronization_controller.list_tenants, True),

    # system routes
    ControllerRoute("GET:/system/info", "", controllers.system_controller.info, True),
    # ControllerRoute("GET:/system/table_info", "", controllers.system_controller.userinfo, True),

    # tenant routes
    ControllerRoute("POST:/tenant/info", "", controllers.tenant_controller.info, True),

    # time routes
    ControllerRoute("GET:/time/info", "", controllers.time_controller.info, True)
]

# adding routes from list to map
for route in routes_list:
    logging.info(f"-----> Adding route, key: {route.key}")
    routes[route.key] = route


# main logic for HTTP route - check authentication and authorization and select route by controller and method
def route_logic(controller_name: str, method_name: str, http_route: ControllerRoute | None, request: Request) -> ResponseSession:
    if http_route is None:
        return ResponseSession.not_found(RequestSession(request, controller_name, method_name), {"status": "NOT_FOUND", "description": "controller or method not found"})
    else:
        try:
            request_session = services.create_session_from_request(request, controller_name, method_name)
            if http_route.require_account:
                if request_session.account_session is None:
                    return ResponseSession.unauthorized_request(request_session, {"status": "INCORRECT_EXPIRED_OR_NO_TOKEN"})
                else:
                    logging.info("Controller Method with authorization")
                    if request_session.has_roles(http_route.roles):
                        resp = http_route.controller_method(request_session)
                        return resp
                    else:
                        # , "required_roles": http_route.roles, "account_roles": request_session.account_permission.roles
                        return ResponseSession.forbidden(request_session,{"status": "FORBIDDEN"})
            else:
                logging.info("Controller Method NO authorization")
                resp = http_route.controller_method(request_session)
                resp.set_end_time()
                return resp
        except Exception as e:
            logging.error("Exception while executing HTTP request, message:" + str(e))
            objects.handle_exception(e)
            return ResponseSession.internal_server_error(RequestSession(request, controller_name, method_name), {'status': "ERROR", "description": "Internal Error, please contact your administrator"})


# main route - handle all HTTP endpoints in this application
@httpflaskapp.route('/api/<controller_name>/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route(controller_name: str, method_name: str) -> Response:
    # route key is made if method, controller name and method name, example: GET:/auth/token
    key = request.method + ":/" + controller_name + "/" + method_name
    # logging.debug("************************* Finding route for name: " + key + ", routes: " + str(len(routes)) + ", lists: " + str(len(routes_list)) + "keys: " + str(routes.keys()))
    http_route = routes.get(key)
    # run routing logic
    http_response = route_logic(controller_name, method_name, http_route, request)
    # just to insert route into DB to table system_request
    objects.handle_request(http_response)
    # return full response
    return http_response.get_final_response()


# start HTTP interface
def start_http_listening() -> None:
    start_duration: timedelta = datetime.datetime.now()-application_start_date
    logging.info(f"Start listening on HTTP 8000, started in {start_duration.total_seconds()} seconds")
    httpflaskapp.run(debug=True, port=8000)
    logging.info("End listening")
