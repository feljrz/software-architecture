from flask import Flask, url_for, request, json, jsonify, make_response, Blueprint
from models import *
from database import *
urls_blueprint = Blueprint('urls', __name__,)

@urls_blueprint.route('/student', methods=['GET'])
def show_students():
    students = hw_get_students()

    # return json.dumps(students)
    return make_response(json.dumps(students))


@urls_blueprint.route('/student', methods=['POST'])
def add_students():
    data = request.get_json()
    hw_add_student(data)
    return make_response(json.dumps(data))

@urls_blueprint.route('/student/<id>', methods=['GET'])
def get_student(id):
    # id = request.args.get('id', type = int)
    student = hw_get_student(id)
    # print(f'1: {request.args[0]}')
    return make_response(json.dumps(student))

# @urls_blueprint.route('/student/<id>', methods=['DELETE'])
# def remove_student(id):
#     hw_remove_student(id, session)
#     res = {'message': f'{id} was removed'}
#     session.close()
#     return make_response(json.dumps(res))


@urls_blueprint.route('/student', methods=['PUT'])
def update_student():
    data = request.get_json()
    hw_update_student(data)
    return make_response(json.dumps(data))

###################################CLASS####################################################
@urls_blueprint.route('/class', methods=['GET'])
def show_classes():
    classes = hw_get_classes()
    return make_response(json.dumps(classes))


@urls_blueprint.route('/class', methods=['POST'])
def add_class():
    data = request.get_json()
    hw_add_class(data)
    return make_response(json.dumps(data))

@urls_blueprint.route('/class/<id>', methods=['GET'])
def get_class(id):
    # id = request.args.get('id', type = int)
    class_ = hw_get_class(id)
    # print(f'1: {request.args[0]}')
    return make_response(json.dumps(class_))

@urls_blueprint.route('/class/<id>', methods=['DELETE'])
def remove_class(id):
    hw_remove_class(id)
    return make_response(json.dumps({'message': id}))


@urls_blueprint.route('/class', methods=['PUT'])
def update_class():
    data = request.get_json()
    hw_update_class(data)
    return make_response(json.dumps(data))

@urls_blueprint.route('/student/<class_name>', methods=['POST'])
def add_student_to_class(class_name):
    data = request.get_json()
    list_class = hw_add_student_to_class(data, class_name)
    return make_response(json.dumps(list_class))


###################################RELATIONSHIP####################################################
@urls_blueprint.route('/classes/student/<student_id>', methods=['GET'])
def get_students_by_class(student_id):
    res = hw_list_student_class(student_id)
    return make_response(json.dumps(res))

@urls_blueprint.route('/note', methods=['POST'])
def add_student_notes():
    data = request.get_json()
    notes = hw_add_student_notes(data)
    return make_response(json.dumps(notes))

@urls_blueprint.route('/notes/student', methods=['GET'])
def list_student_notes():
    notes = hw_list_student_note()
    return make_response(json.dumps(notes))



