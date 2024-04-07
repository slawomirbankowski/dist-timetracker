from base.base_objects import objects
from service.service_base import service_base, service_thread_base
from dao.daos import daos
import psutil


class SystemStateService(service_thread_base):
    def __init__(self):
        super().__init__()

    # get name of base object
    def get_base_object_name(self) -> str:
        return "SystemStateService"

    # work in separated thread
    def thread_work(self, tick: int) -> bool:
        process = psutil.Process()
        mi = process.memory_info()
        daos.system_state_dao_instance.insert_row_random_uid("", mi.rss, mi.vms, len(objects.all_objects), daos.system_instance_uid)
        daos.system_instance_dao_instance.update_touch_by_uid(daos.system_instance_dto.system_instance_uid)
        return True
