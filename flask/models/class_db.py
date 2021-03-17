from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, relationship
from .model import Base, Class, Class
import json
import os 

# basedir = os.path.abspath(os.path.dirname(__file__))
# engine = create_engine('sqlite:///' +os.path.join(basedir,'class_s.db'), echo=True)
# Base.metadata.create_all(bind=engine)



def create_session():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_url = 'sqlite:///' +os.path.join(basedir,'class_s.db')

    if not db_url:
        raise DatabaseError

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    created_session = sessionmaker(bind=engine)
    return created_session()

def hw_add_class(class_, session):
    print('\n\n---------------------------------hw_add_class_------------------------------------\n\n')
    for class_id, class_name in [class_.values()]:
        session.add(Class(class_id=class_id, class_name=class_name))
    session.commit()


def hw_get_classes(session):
    print('\n\n---------------------------------hw_get_classes_------------------------------------\n\n')
    class_s = session.query(Class).order_by(Class.class_name.asc()).all()
    list_class_ = [{'class_id': class_.class_id, 
                    'class_name': class_.class_name} for class_ in class_s]

    return list_class_
    # return session.query(Class).order_by(Class.finame.asc()).all()

def hw_get_class(id, session):
    print('\n\n---------------------------------hw_get_class_------------------------------------\n\n')
    class_s = session.query(Class).filter_by(class_id=id).all()
    list_class_ = [{'class_id': class_.class_id, 
                    'class_name': class_.class_name} for class_ in class_s]
        
    return list_class_
    # return class_

def hw_remove_class(id, session):
    print('\n\n---------------------------------hw_remove_class_------------------------------------\n\n')
    class_ = session.query(Class).filter(Class.class_id == id).first()
    session.delete(class_)
    session.commit()

def hw_update_class(class_, session):
    print('\n\n---------------------------------hw_update_class_------------------------------------\n\n')
    class_id = class_['class_id']
    curr_class_ = hw_get_class(class_id, session)[0]
   

    hw_remove_class(curr_class_['class_id'], session)
    hw_add_class(class_, session)
    session.commit()


# session = _create_session()





