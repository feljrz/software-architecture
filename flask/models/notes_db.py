from sqlalchemy.exc import DatabaseError
from .model import Base, Class, Student, Note
from .student_db import hw_get_student
from .class_db import hw_get_class

import json


def hw_add_student_notes(note, session):
    for id, student_id, class_id, note in [note.values()]:
        session.add(Note(note_id=id, student_id= student_id, class_id= class_id, note= note))
        print('\n\n---------------------------------add_student_note------------------------------------\n\n')

        student = hw_get_student(student_id, session)
        class_ = hw_get_class(class_id, session)

        print(student)
        print(class_)
        print('\n\n---------------------------------add_student_note------------------------------------\n\n')

    session.commit()
    return None
    



# def get_student_notes(student_id, session):
#     student = hw_get_student(student_id, session)
#     session.query(Notes)

