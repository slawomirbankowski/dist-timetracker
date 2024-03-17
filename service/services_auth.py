from service.service_base import service_base, service_thread_base
from dao.daos import daos


class LoginService(service_thread_base):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "LoginService"
    def login(self):
        print("Login")

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True


class PermissionService(service_thread_base):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "PermissionService"
    def get_permissions(self):
        print("Permissions")

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True


class KeyService(service_thread_base):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "KeyService"
    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True
    def get_keys(self):
        print("Login")
