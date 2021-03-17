from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, relationship
from .model import Base, Class, Student
import json
import os 

# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine('sqlite:///' +os.path.join(basedir,'students.db'), echo=True)
# Base.metadata.create_all(bind=engine)



def create_session():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_url = 'sqlite:///' +os.path.join(basedir,'students.db')

    if not db_url:
        raise DatabaseError

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    created_session = sessionmaker(bind=engine)
    return created_session()

def hw_add_student(student, session):
    print('\n\n---------------------------------hw_add_student------------------------------------\n\n')
    for student_id, first_name, last_name in [student.values()]:
        # session.add(Student(student_id=student['id'], first_name=student['first_name'], last_name=student['last_name']))
        session.add(Student(student_id=student_id, first_name=first_name, last_name=last_name))
    session.commit()


def hw_get_students(session):
    print('\n\n---------------------------------hw_get_students------------------------------------\n\n')
    students = session.query(Student).order_by(Student.first_name.asc()).all()
    list_student = [{'student_id': student.student_id, 
                    'first_name': student.first_name, 
                    'last_name':student.last_name} for student in students]

    return list_student
    # return session.query(Student).order_by(Student.finame.asc()).all()

def hw_get_student(id, session):
    print('\n\n---------------------------------hw_get_student------------------------------------\n\n')
    students = session.query(Student).filter_by(student_id=id).all()
    list_student = [{'student_id': student.student_id, 
                    'first_name': student.first_name, 
                    'last_name':student.last_name} for student in students]
        
    return list_student
    # return student

def hw_remove_student(id, session):
    print('\n\n---------------------------------hw_remove_student------------------------------------\n\n')
    student = session.query(Student).filter(Student.student_id == id).first()
    session.delete(student)
    session.commit()

def hw_update_student(student, session):
    print('\n\n---------------------------------hw_update_student------------------------------------\n\n')
    student_id = student['student_id']
    curr_student = hw_get_student(student_id, session)[0]
   

    hw_remove_student(curr_student['student_id'], session)
    hw_add_student(student, session)
    session.commit()


# session = _create_session()





