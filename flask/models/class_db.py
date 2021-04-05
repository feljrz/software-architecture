from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, relationship
from .models import Base, Class, Student
import json
import os 

# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine('sqlite:///' +os.path.join(basedir,'class_s.db'), echo=True)
# Base.metadata.create_all(bind=engine)

def populate_class(class_):
    list_class = [{'id': class_.id, 
                    'class_name': class_.class_name} for class_ in class_]
    return list_class              

def hw_add_class(class_, session):
    print('\n\n---------------------------------hw_add_class_------------------------------------\n\n')
    print(class_)
    class_name = class_['class_name']
    session.add(Class(class_name=class_name))
    session.commit()


def hw_get_classes(session):
    print('\n\n---------------------------------hw_get_classes_------------------------------------\n\n')
    classes = session.query(Class).order_by(Class.class_name.asc()).all()
    list_class = populate_class(classes)

    return list_class
    # return session.query(Class).order_by(Class.finame.asc()).all()

def hw_get_class(id, session):
    # print('\n\n---------------------------------hw_get_class_------------------------------------\n\n')
    classes = session.query(Class).filter_by(id=id).all()
    list_class = populate_class(classes)
        
    return list_class
    # return class_

def hw_remove_class(id, session):
    # print('\n\n---------------------------------hw_remove_class_------------------------------------\n\n')
    class_ = session.query(Class).filter(Class.id == id).first()
    session.delete(class_)
    session.commit()

    
def hw_update_class(class_, session):
    # print('\n\n---------------------------------hw_update_class_------------------------------------\n\n')
   
    curr_class_ = session.query(Class).filter(Class.class_name == class_['class_name']).one_or_none()
   

    hw_remove_class(curr_class_.class_name, session)
    hw_add_class(class_, session)
    session.commit()

def hw_get_students_by_class(session):
    students = session.query(Student.student_id, Student.first_name, Student.last_name).join(Class.students).all()



    list_students = [{'student_id': student.student_id, 
                    'first_name': student.first_name, 
                    'last_name':student.last_name} for student in students]
    return list_students


def hw_add_student_to_class(student, class_name, session):
    # print('\n\n---------------------------------hw_add_student_to_class------------------------------------\n\n')
    print(class_name)
    class_ = session.query(Class).filter(Class.class_name == class_name).one_or_none()
   
    student_obj = session.query(Student).filter_by(first_name=student['first_name']).first()

    if(len(student_obj.notes) > 3):
        return [{'message': 'Student already has 3'}]

    class_.students.append(student_obj)
    session.add(class_)
    session.commit()  

    list_class = populate_class([class_])
    session.close()
    return list_class






