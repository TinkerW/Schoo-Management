# FULL
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

from database import Base


# Таблица студентов
class Student(Base):
    __tablename__ = 'student'
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    class_number = Column(String, nullable=False)
    school_number = Column(Integer, nullable=False)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


# Таблица студентов
class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    subject_name = Column(String, nullable=False)
    school_number = Column(Integer, nullable=False)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)


# # Таблица предметов
class Subject(Base):

    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)

    st_id = Column(Integer, ForeignKey('student.id'))

    subject_name = Column(String)
    subject_order = Column(Integer)

    mark_fk = relationship(Student, Teacher, lazy='subquery')
    st_fk = relationship(Student, Teacher, lazy='subquery')


# Таблица оценок
#class Mark(Base):
#    __tablename__ = 'marks'
#    mark_id = Column(Integer, primary_key=True, autoincrement=True)
#    subject_mark = Column(String, nullable = False)
#    mark = Column(Float)
#
#    status = Column(Boolean, default=True)#
#
#    exp_date = Column(DateTime)
#
#    mark_fk = relationship(Student, Teacher, lazy='subquery')

