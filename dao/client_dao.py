import dao.dao_connection

class ClientDao:

    daoConn = dao.dao_connection.daoConn
    def __init__(self):
        print("Starting client DAO")

    def getClients(self):
        return ''
    def addClient(self, client):
        print('Adding client to DB')
    def removeClient(self, clientName):
        print('Removing client from DB')