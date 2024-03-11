from flask import Flask, jsonify, request, abort

from dao.daos_instances import *

print('Flask starting app')
app = Flask(__name__)

tasks = [
   {
       'id': 1,
       'title': u'Buy groceries',
       'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
       'done': False
   },
   {
       'id': 2,
       'title': u'Learn Python',
       'description': u'Need to find a good Python tutorial on the web',
       'done': False
   }
]

pong = "pong"
version = {
    'version': 1.0,
    'applicationName': 'TimeTracker'
}

@app.route('/api/ping', methods=['GET'])
def ping():
   return jsonify({'ping': pong})

@app.route('/api/version', methods=['GET'])
def version():
   return jsonify(version)

@app.route('/api/clients', methods=['GET'])
def get_clients():
   print(request.headers)
   return jsonify({'tasks': tasks})

@app.route('/api/clients-active', methods=['GET'])
def get_clients_active():
   return jsonify({'tasks': tasks})

@app.route('/api/account-division-all', methods=['GET'])
def get_account_division_all():
    #request.content_type
    #request.content_length
   return jsonify(account_division_dao_instance.get_items_all(1000).dtos)


def startHttpListening():
    print('Start listening')
    app.run(debug=True, port=8000)
    print('End listening')
