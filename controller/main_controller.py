from flask import Flask, jsonify, request, abort

print('Flask starting app')
app = Flask(__name__)


clients = [
]

# TODO: change this implementation

@app.route('/api/clients', methods=['GET'])
def get_clients():
   print(request.headers)
   return jsonify({'tasks': clients})

@app.route('/api/clients-active', methods=['GET'])
def get_clients_active():
   return jsonify({'tasks': clients})
