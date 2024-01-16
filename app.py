from flask import Flask, abort, request
from hallo import name, add_name as add_name_handler, update_name as update_name_handler, delete_name as delete_name_handler
from hallo import view_name 

app = Flask(__name__)


@app.route('/hallo')
def hallo() :
    return name()

@app.route('/create', methods=['POST'])
def add_name():
    return add_name_handler()

@app.route("/update/<id>", methods=['PATCH'])
def update_name(id):
    return update_name_handler(id)

@app.route("/delete/<id>", methods=['DELETE'])
def delete_name(id):
    return delete_name_handler(id)

@app.route("/detail/<id>", methods=['GET'])
def detail_name(id):
    return view_name(id)

if __name__ == '__main__':
    app.run(debug=True)