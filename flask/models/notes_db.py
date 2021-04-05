from sqlalchemy.exc import DatabaseError
from .models import Base, Class, Student, Note
from .student_db import hw_get_student
from .class_db import hw_get_class

import json

def populate_note(note_obj):
    list_note = [{"id":note.id, "student_id": note.student_id,
                "class_id": note.class_id, "note": note.note} for note in note_obj]
    return list_note

# def hw_add_student_notes(note, session):
#     for student_id, class_id, note in [note.values()]:
        
#         note = Note(student_id= student_id, class_id= class_id, note= note)
#         print(note)
#         student_obj = session.query(Student).filter(Student.id == student_id).first()
            
#         class_obj = session.query(Class).filter(Class.id == class_id).first()

#         student_obj.notes.append(note)
#         class_obj.notes.append(note)
#         session.add(student_obj)
#         session.add(class_obj)
#         session.add(note)
#         class_notes = class_obj.notes
#         # #Class notes
#         # for note_obj in class_notes:
#         #     print(note_obj.note)


#     notes = populate_note([note])
#     # notes = None
#     session.commit()
#     return notes

def hw_add_student_notes(request, session):
    print('\n\n---------------------------------ADD_STUDENT------------------------------------\n\n')
    print(request)
    students = session.query(Student).filter(Student.id == request['student_id']).all()
    classes = session.query(Class).filter(Class.id == request['class_id']).all()
    new_note = Note()
    new_note.student_id = request['student_id']
    new_note.class_id = request['class_id']
    new_note.students = [student for student in students]
    new_note.classes = [class_ for class_ in classes]
    new_note.note = request['note']
    session.add(new_note)
    session.commit()
    note = populate_note([new_note])
    return note




def hw_list_student_note(session):

    students = session.query(Student).order_by(Student.first_name.asc()).all()
    notes = []
    for student in students:
        student_notes = student.notes
        
        print(student.first_name)
        notes.append(populate_note(student_notes))
        for note_obj in student_notes:
            print(note_obj.note)
    
    return notes

def hw_relatorio(session):
    students = session.query(Student).order_by(Student.first_name.asc()).all()
    print('\n\n---------------------------------RELATORIO------------------------------------\n\n')
    relatorio = []
    for student in students:
        student_notes = student.notes 
        for note_obj in student_notes:
            class_name = hw_get_class(note_obj.class_id, session)[0]['class_name']
            # print(class_name)
            echo = f'\n Disciplina | Nota \n {class_name}    {note_obj.note} \n\n -----------------'
            relatorio.append(echo)
            # print(note_obj.note)
    
        relatorio.append(f'\n ALUNO(A): {student.first_name}')
    
    for e in relatorio:
        print(e)

    