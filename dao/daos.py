import dao.dao_connection
from typing import TypeVar, Generic, List

from dto.dtos import ModelBase, BaseDto

T = TypeVar('T')



class BaseDao(Generic[T]):
    def __init__(self, model: ModelBase, dto: BaseDto):
        print("Starting client DAO")

    def getClients(self):
        return ''
    def addClient(self, client):
        print('Adding client to DB')
    def removeClient(self, clientName):
        print('Removing client from DB')

class ClientDao(BaseDao):
    def __init__(self):
        print("Starting client DAO")

    def getClients(self):
        return ''
    def addClient(self, client):
        print('Adding client to DB')
    def removeClient(self, clientName):
        print('Removing client from DB')

    daoConn = dao.dao_connection.daoConn
