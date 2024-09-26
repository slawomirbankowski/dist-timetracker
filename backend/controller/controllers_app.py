from __future__ import annotations

from datetime import timedelta

from flask import Flask, jsonify, request, abort, Request, Response
import logging
from logging import config
import base.base_objects
from base.base_constants import application_start_date, Roles
from service import services
from dao.daos_instances import *
from dao.daos import daos
from controller.controllers import controllers
from controller.controller_base import RequestSession, ControllerRoute, ResponseSession

# main Flask application
httpflaskapp: Flask = base.base_objects.httpflaskapp

# all routes - map by key, key of the route should be : METHOD:/version/controller/method
# example: GET:/v1/service/ping
routes: dict[str, ControllerRoute] = {}


# HTTP endpoint that is listing all endpoints
def endpoints(session: RequestSession) -> ResponseSession:
    routes_info = list(map(lambda key: routes[key].to_dict(), routes))
    return ResponseSession.ok(session, { "endpoints": routes_info})


# all routes - list of available routes
routes_list: list[ControllerRoute] = [

    # account routes
    ControllerRoute("PUT:/v1/account/create", "", controllers.account_controller.create_account, True),
    ControllerRoute("DELETE:/v1/account/deactivate", "", controllers.account_controller.create_account, True),
    ControllerRoute("GET:/v1/account/list", "", controllers.account_controller.list_accounts, True),
    ControllerRoute("GET:/v1/account/get_account_by_uid", "", controllers.account_controller.list_accounts, True),

    # authentication routes
    ControllerRoute("GET:/v1/auth/set-password", "Set password for any user", controllers.auth_controller.set_password, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/change-password", "Set password for currently logged user", controllers.auth_controller.change_password, True),
    ControllerRoute("GET:/v1/auth/check-password", "", controllers.auth_controller.check_password, True),
    ControllerRoute("GET:/v1/auth/produce-hash", "", controllers.auth_controller.produce_hash),
    ControllerRoute("GET:/v1/auth/produce-password-tab", "", controllers.auth_controller.produce_passwords_tab),

    ControllerRoute("POST:/v1/auth/reset-request", "Request to reset password", controllers.auth_controller.request_password, False),
    ControllerRoute("POST:/v1/auth/reset-check", "Check request token for password", controllers.auth_controller.reset_check, False),
    ControllerRoute("POST:/v1/auth/reset-password", "Reset password", controllers.auth_controller.reset_password, False),

    ControllerRoute("GET:/v1/auth/get-auth-method", "Get authentication method by account name or email or UID", controllers.auth_controller.get_auth_method),
    ControllerRoute("GET:/v1/auth/token", "Create token with authentication method", controllers.auth_controller.token),
    ControllerRoute("POST:/v1/auth/token", "Create token with authentication method",  controllers.auth_controller.token),
    ControllerRoute("PUT:/v1/auth/token", "Create token with authentication method", controllers.auth_controller.token),
    ControllerRoute("PATCH:/v1/auth/token", "Create token with authentication method", controllers.auth_controller.token),
    ControllerRoute("POST:/v1/auth/logout", "Invalidate session", controllers.auth_controller.logout),
    ControllerRoute("DELETE:/v1/auth/logout", "Invalidate session", controllers.auth_controller.logout),

    ControllerRoute("GET:/v1/auth/sessions-latest", "List sessions", controllers.auth_controller.sessions_db_latest, True, {"ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/sessions", "List sessions", controllers.auth_controller.sessions_db_list, True, {"ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/sessions-memory", "List sessions", controllers.auth_controller.sessions_list, True, {"ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/sessions-by-account", "List sessions for selected account", controllers.auth_controller.sessions_by_account, True, {"ClientAdministrator"}),

    ControllerRoute("GET:/v1/auth/myself", "", controllers.auth_controller.myself, True),
    ControllerRoute("GET:/v1/auth/userinfo", "", controllers.auth_controller.userinfo, True),
    ControllerRoute("POST:/v1/auth/reload-session", "", controllers.auth_controller.reload_session, True),

    ControllerRoute("GET:/v1/auth/roles", "", controllers.auth_controller.roles_list, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/roles-info", "", controllers.auth_controller.roles_list, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/roles-thin", "", controllers.auth_controller.roles_list_thin, True,  {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/auth/roles-hierarchy", "", controllers.auth_controller.roles_hierarchy, True,  {"SystemAdministrator", "ClientAdministrator"}),

    ControllerRoute("GET:/v1/auth/menu", "", controllers.auth_controller.menu_for_user, True),
    ControllerRoute("GET:/v1/auth/menu-full", "", controllers.auth_controller.menu_full, True),
    # client routes
    ControllerRoute("POST:/v1/client/info", "", controllers.client_controller.info, True),
    # ControllerRoute("GET:/client/list", "", controllers.client_controller.list_clients, True),

    # competency routes
    # ControllerRoute("POST:/v1/competency/info", "", controllers.competency_controller.info, True),
    # ControllerRoute("GET:/v1/competency/list", "", controllers.competency_controller.list_connections(), True),

    # connection routes
    ControllerRoute("POST:/v1/connection/info", "", controllers.connection_controller.info, True),
    # ControllerRoute("GET:/connection/list", "", controllers.connection_controller.list_connections, True),

    # event routes
    ControllerRoute("POST:/v1/event/info", "", controllers.event_controller.info, True),
    # ControllerRoute("GET:/v1/event/list", "", controllers.event_controller.list_events, True),

    # invoice routes
    ControllerRoute("POST:/v1/invoice/info", "", controllers.invoice_controller.info, True),
    # ControllerRoute("GET:/invoice/list", "", controllers.invoice_controller.list_tenants, True),

    # object routes
    ControllerRoute("GET:/v1/object/info", "", controllers.object_controller.info, True),
    ControllerRoute("GET:/v1/object/count", "", controllers.object_controller.get_object_count, True),
    ControllerRoute("GET:/v1/object/get_list", "", controllers.object_controller.get_objects_list, True),
    ControllerRoute("GET:/v1/object/get_by_uid", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("GET:/v1/object/get_rich_by_uid", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("GET:/v1/object/search", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("POST:/v1/object/create", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("PATCH:/v1/object/update", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("PATCH:/v1/object/check", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("DELETE:/v1/object/delete", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("DELETE:/v1/object/deactivate", "", controllers.object_controller.get_object_by_uid, True),
    ControllerRoute("POST:/v1/object/action", "Run defined action for object", controllers.object_controller.get_object_by_uid, True),

    # monitor routes
    ControllerRoute("POST:/v1/monitor/info", "", controllers.monitor_controller.info, True),
    # ControllerRoute("GET:/monitor/list", "", controllers.monitor_controller.list_tenants, True),

    # process routes
    ControllerRoute("POST:/v1/process/info", "", controllers.process_controller.info, True),
    # ControllerRoute("GET:/process/list", "", controllers.process_controller.list_tenants, True),

    # project routes
    ControllerRoute("POST:/v1/project/info", "", controllers.project_controller.info, True),
    # ControllerRoute("GET:/project/list", "", controllers.project_controller.list_tenants, True),

    # report routes
    ControllerRoute("POST:/v1/report/info", "", controllers.report_controller.info, True),
    # ControllerRoute("GET:/report/list", "", controllers.report_controller.list_tenants, True),

    # service routes
    ControllerRoute("GET:/v1/service/ping", "Just ping to check", controllers.service_controller.ping),
    ControllerRoute("GET:/v1/service/version", "Check version of current application", controllers.service_controller.version),
    ControllerRoute("GET:/v1/service/dao", "Get DAO", controllers.service_controller.dao, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/service/connections", "", controllers.service_controller.connections, True),
    ControllerRoute("GET:/v1/service/objects", "All management objects for current application instance", controllers.service_controller.objs, True),
    ControllerRoute("GET:/v1/service/models", "List models", controllers.service_controller.models, True),
    ControllerRoute("GET:/v1/service/endpoints", "List of HTTP endpoints", endpoints, True),
    ControllerRoute("GET:/v1/service/threads", "Threads", controllers.service_controller.threads, True, {"SystemAdministrator", "ClientAdministrator"}),
    ControllerRoute("GET:/v1/service/caches", "", controllers.service_controller.caches, True),
    ControllerRoute("GET:/v1/service/settings", "", controllers.service_controller.settings),
    ControllerRoute("GET:/v1/service/settings-system", "", controllers.service_controller.settings),

    # storage routes
    ControllerRoute("POST:/v1/storage/info", "", controllers.storage_controller.info, True),
    # ControllerRoute("GET:/storage/list", "", controllers.storage_controller.list_tenants, True),

    # synchronization routes
    ControllerRoute("POST:/v1/synchronization/info", "", controllers.synchronization_controller.info, True),
    # ControllerRoute("GET:/synchronization/list", "", controllers.synchronization_controller.list_tenants, True),

    # system routes
    ControllerRoute("GET:/v1/system/info", "", controllers.system_controller.info, True),
    # ControllerRoute("GET:/system/table_info", "", controllers.system_controller.userinfo, True),

    # tenant routes
    ControllerRoute("GET:/v1/tenant/info", "", controllers.tenant_controller.info, True),
    ControllerRoute("GET:/v1/tenant/list", "List of all existing tenants", controllers.tenant_controller.list_tenants, True, {Roles.ClientAdministrator, Roles.TenantViewer, Roles.TenantAdministrator}),
    ControllerRoute("GET:/v1/tenant/list_thin", "Simple list of all existing tenants", controllers.tenant_controller.list_tenants_thin, True, {Roles.ClientAdministrator, Roles.TenantViewer, Roles.TenantAdministrator}),
    ControllerRoute("PUT:/v1/tenant/create", "Create new tenant", controllers.tenant_controller.create_tenant, True, {Roles.ClientAdministrator, Roles.TenantViewer, Roles.TenantAdministrator}),
    ControllerRoute("PUT:/v1/tenant/dictionaries", "List all dictionaries needed to create new tenant", controllers.tenant_controller.tenant_dictionaries, True,
                    {Roles.ClientAdministrator, Roles.TenantViewer, Roles.TenantAdministrator}),



    # time routes
    ControllerRoute("GET:/v1/time/info", "", controllers.time_controller.info, True)
]

# adding routes from list to map
for route in routes_list:
    logging.info(f"-----> Adding route, key: {route.key}")
    routes[route.key] = route


def route_logic(version_name: str, controller_name: str, method_name: str, http_route: ControllerRoute | None, route_request: Request) -> ResponseSession:
    """main logic for HTTP route - check authentication and authorization and select route by controller and method"""
    if http_route is None:
        return ResponseSession.not_found(RequestSession(route_request, controller_name, method_name), {"status": "NOT_FOUND", "description": "controller or method not found"})
    else:
        try:
            request_session: RequestSession = services.create_session_from_request(route_request, controller_name, method_name)
            if http_route.require_account:
                if request_session.account_session is None:
                    return ResponseSession.unauthorized_request(request_session, {"status": "INCORRECT_EXPIRED_OR_NO_TOKEN"})
                else:
                    logging.info("Controller Method with authorization - check roles")
                    if request_session.has_roles(http_route.roles):
                        resp = http_route.controller_method(request_session)
                        return resp
                    else:
                        # , "required_roles": http_route.roles, "account_roles": request_session.account_permission.roles
                        return ResponseSession.forbidden(request_session, {"status": "FORBIDDEN"})
            else:
                logging.info("Controller Method NO authorization")
                resp = http_route.controller_method(request_session)
                resp.set_end_time()
                return resp
        except Exception as e:
            logging.error("Exception while executing HTTP request, message:" + str(e))
            objects.handle_exception(e)
            return ResponseSession.internal_server_error(RequestSession(route_request, controller_name, method_name), {'status': "ERROR", "description": "Internal Error, please contact your administrator"})


@httpflaskapp.route('/api/<version_name>/<controller_name>/<method_name>', methods=['GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def route(version_name: str, controller_name: str, method_name: str) -> Response:
    """main route - handle all HTTP endpoints in this application"""
    # route key is made if method, controller name and method name, example: GET:/auth/token
    key = f"{request.method}:/{version_name}/{controller_name}/{method_name}"
    # logging.debug("************************* Finding route for name: " + key + ", routes: " + str(len(routes)) + ", lists: " + str(len(routes_list)) + "keys: " + str(routes.keys()))
    http_route = routes.get(key)
    # run routing logic
    http_response = route_logic(version_name, controller_name, method_name, http_route, request)
    # just to insert route into DB to table system_request
    objects.handle_request(http_response)
    # return full response
    return http_response.get_final_response()


def start_http_listening() -> None:
    """start HTTP interface"""
    start_duration: timedelta = datetime.datetime.now()-application_start_date
    logging.info(f"Start listening on HTTP 8000, started in {start_duration.total_seconds()} seconds")
    httpflaskapp.run(debug=True, host='0.0.0.0', port=8000)
    logging.info("End listening")
