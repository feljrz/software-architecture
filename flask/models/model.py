from sqlalchemy import Column, Integer, String, Table, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

student_class = Table(
    'student_class', Base.metadata,
    Column('student_id', Integer, ForeignKey("student.student_id")),
    Column('class_id', Integer, ForeignKey("class.class_id")),
)

class Student(Base):
    __tablename__ = 'student'
    student_id = Column('student_id', Integer, primary_key=True)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String)


class Class(Base):
    __tablename__ = 'class'
    class_id = Column('class_id', Integer, primary_key=True)
    class_name = Column(String)





