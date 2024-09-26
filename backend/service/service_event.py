from service.services_base import ServiceThreadBase


class EventService(ServiceThreadBase):
    def __init__(self):
        super().__init__()
    # get name of base object
    def get_base_object_name(self) -> str:
        return "AccountService"
    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        return True
