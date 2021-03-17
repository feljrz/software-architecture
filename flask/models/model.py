from sqlalchemy import Column, Integer, String, Table, Sequence, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

student_class = Table(
    'student_class', Base.metadata,
    Column('student_id', Integer, ForeignKey("student.id")),
    Column('class_id', Integer, ForeignKey("class.id")),
)


# student_notes = Table(
#     'student_notes', Base.metadata,
#     Column('id', Integer, ForeignKey('note.id')),
#     Column('student_id', Integer, ForeignKey('student.student_id')),
#     Column('class_id', Integer, ForeignKey('class.class_id')),
# )


student_notes = Table(
    'student_notes', Base.metadata,
    Column('note_id', Integer, ForeignKey("note.id")),
    Column('student_id', Integer, ForeignKey("student.id")),
    Column('class_id', Integer, ForeignKey("class.id")),
)

class Note(Base):
    __tablename__ = 'note'
    id = Column('id', Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    class_id = Column('class_id', Integer, ForeignKey("class.id"))
    students = relationship("Student", secondary=student_notes, back_populates="notes")
    classes = relationship("Class", secondary=student_notes, back_populates="notes")
    note = Column(Float)


class Student(Base):
    __tablename__ = 'student'
    id = Column('id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    classes = relationship("Class", secondary=student_class, back_populates="students")
    notes = relationship("Note", secondary=student_notes, back_populates="students")
    last_name = Column('last_name', String)


class Class(Base):
    __tablename__ = 'class'
    id = Column('id', Integer, primary_key=True)
    students = relationship("Student", secondary=student_class, back_populates="classes")
    notes = relationship("Note", secondary=student_notes, back_populates="classes")

    class_name = Column(String)

    




