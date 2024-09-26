import custom
from custom.identity_type import identity_types

def create_identity_by_class_name(class_name: str) -> any:
    class_type = getattr(custom.identity_type.identity_types, class_name)
    class_object = class_type()
    return class_object


