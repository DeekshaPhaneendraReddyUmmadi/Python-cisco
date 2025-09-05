from flask import Flask, request, jsonify
from repo import read_all, create_employee, read_by_id, update_by_id, delete_by_id

app = Flask(__name__)

@app.route("/employees", methods=['GET'])
def read_employees():
    employees = read_all()
    return jsonify(employees)

@app.route("/employees", methods=['POST'])
def createEmployee():
    employee = request.get_json()
    create_employee(employee['id'], employee['name'])
    return jsonify(employee)

@app.route("/employees/<id>", methods=['GET'])
def find_by_id(id):
    id = int(id)
    emp = read_by_id(id)
    return jsonify(emp)

@app.route("/employees/<id>", methods=['PUT'])
def update(id):
    id = int(id)
    emp = request.get_json()
    update_by_id(id, emp['name'])
    updatedEmp = read_by_id(id)
    return jsonify(updatedEmp)


@app.route("/employees/<id>", methods=['DELETE'])
def delete(id):
    id = int(id)
    delete_by_id(id)
    return jsonify("Deleted")



app.run(debug=True)