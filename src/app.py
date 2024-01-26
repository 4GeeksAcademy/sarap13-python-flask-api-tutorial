from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    new_todo = {
       "done": request_body["done"], 
       "label": request_body["label"]
    }
    todos.append(new_todo)
    response_body = {
       "new_todo" : new_todo
    }
    return jsonify(response_body), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Eliminamos el todo en la posicion dada
    del todos[position]
    response_body = {
    "done": True
    }
    return jsonify(response_body), 200


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)