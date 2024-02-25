import datetime
from dataclasses import dataclass


class ModelBase:
    tableName: string = ""
    idColumnName: string = ""
    keyColumnName: string = ""



@dataclass(frozen=True)
class BaseDto:
    id: int = 0
    created_date: datetime = datetime.UTC
    last_updated_date: datetime
    def __init__(self):
        print("Nothing to be done here")

class ClientDto:
    def __init__(self):
        print("Nothing to be done here")
