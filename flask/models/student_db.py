from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, relationship
from .models import Base, Class, Student
from .class_db import populate_class
import json
import os
from database import SessionLocal

# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine('sqlite:///' +os.path.join(basedir,'students.db'), echo=True)
# Base.metadata.create_all(bind=engine)



# def create_session():
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     db_url = 'sqlite:///' + os.path.join(basedir,'students.db')

#     if not db_url:
#         raise DatabaseError

    # engine = create_engine(db_url, echo=True)
    # Base.metadata.create_all(engine)
    # created_session = sessionmaker(bind=engine, autoflush=False)
    # return created_session()

def hw_add_student(student):
    session = SessionLocal()
    # print('\n\n---------------------------------hw_add_student------------------------------------\n\n')
    for first_name, last_name in [student.values()]:
        # session.add(Student(id=student['id'], first_name=student['first_name'], last_name=student['last_name']))
        session.add(Student(first_name=first_name, last_name=last_name))
    session.commit()
    session.close()


def hw_get_students():
    # print('\n\n---------------------------------hw_get_students------------------------------------\n\n')
    session = SessionLocal()
    students = session.query(Student).order_by(Student.first_name.asc()).all()
    list_student = [{'id': student.id, 
                    'first_name': student.first_name, 
                    'last_name':student.last_name} for student in students]
    session.close()
    return list_student
    # return session.query(Student).order_by(Student.finame.asc()).all()

def hw_get_student(id):
    # print('\n\n---------------------------------hw_get_student------------------------------------\n\n')
    session = SessionLocal()
    students = session.query(Student).filter_by(id=id).all()
    list_student = [{'id': student.id, 
                    'first_name': student.first_name, 
                    'last_name':student.last_name} for student in students]
    session.close()
        
    return list_student
    # return student

def hw_remove_student(id):
    # print('\n\n---------------------------------hw_remove_student------------------------------------\n\n')
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == id).first()
    session.delete(student)
    session.commit()
    session.close()

def hw_update_student(student):
    session = SessionLocal()
    curr_student = session.query(Student).filter(Student.first_name == student['first_name']).one_or_none()
    # print('\n\n---------------------------------hw_update_student------------------------------------\n\n')
    # print(curr_student.id)
    # print(student['first_name'])
    # print('\n\n---------------------------------hw_update_student------------------------------------\n\n')
    hw_remove_student(curr_student.id) # **
    hw_add_student(student) # **
    session.commit()
    session.close()

def hw_list_student_class(student_id):
    session = SessionLocal()
    student = session.query(Student).filter(Student.id == student_id).first()
    list_class = populate_class(student.classes)
    session.close()

    return list_class










