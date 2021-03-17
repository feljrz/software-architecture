from flask import Flask, url_for, request, json, jsonify, make_response
# from models import (hw_get_students_by_class, hw_list_student_class, hw_add_student_to_class, hw_get_students, create_session, hw_add_student, hw_get_student, hw_remove_student, hw_update_student, 
# hw_add_class, hw_get_classes,hw_get_class, hw_remove_class, hw_update_class, create_session)

from models import *

app = Flask(__name__)

@app.route('/student', methods=['GET'])
def show_students():
    students = hw_get_students(session)

    session.close()
    # return json.dumps(students)
    return make_response(json.dumps(students))


@app.route('/student', methods=['POST'])
def add_students():
    data = request.get_json()
    hw_add_student(data, session)
    session.close()
    return make_response(json.dumps(data))

@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    # id = request.args.get('id', type = int)
    student = hw_get_student(id, session)
    # print(f'1: {request.args[0]}')
    return make_response(json.dumps(student))

@app.route('/student/<id>', methods=['DELETE'])
def remove_student(id):
    hw_remove_student(id, session)
    session.close()
    return make_response(json.dumps({'message': id}))


@app.route('/student', methods=['PUT'])
def update_student():
    data = request.get_json()
    hw_update_student(data, session)
    session.close()
    return make_response(json.dumps(data))

###################################CLASS####################################################
@app.route('/class', methods=['GET'])
def show_classes():
    classes = hw_get_classes(session)

    session.close()
    return make_response(json.dumps(classes))


@app.route('/class', methods=['POST'])
def add_class():
    data = request.get_json()
    hw_add_class(data, session)
    session.close()
    return make_response(json.dumps(data))

@app.route('/class/<id>', methods=['GET'])
def get_class(id):
    # id = request.args.get('id', type = int)
    class_ = hw_get_class(id, session)
    # print(f'1: {request.args[0]}')
    return make_response(json.dumps(class_))

@app.route('/class/<id>', methods=['DELETE'])
def remove_class(id):
    hw_remove_class(id, session)
    session.close()
    return make_response(json.dumps({'message': id}))


@app.route('/class', methods=['PUT'])
def update_class():
    data = request.get_json()
    hw_update_class(data, session)
    session.close()
    return make_response(json.dumps(data))

@app.route('/student/<class_name>', methods=['POST'])
def add_student_to_class(class_name):
    data = request.get_json()
    list_class = hw_add_student_to_class(data, class_name, session)
    return make_response(json.dumps(list_class))


###################################RELATIONSHIP####################################################
@app.route('/classes/student/<student_id>', methods=['GET'])
def get_students_by_class(student_id):

    res = hw_list_student_class(student_id, session)
    return make_response(json.dumps(res))

@app.route('/note', methods=['POST'])
def add_student_notes():
    data = request.get_json()
    hw_add_student_notes(data, session)
    return make_response(json.dumps({"message": "sera"}))

if __name__ == '__main__':
    session = create_session()
    app.run(debug=True)
