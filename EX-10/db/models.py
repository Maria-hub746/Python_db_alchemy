from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    students = relationship('Student', back_populates='group')


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(255), nullable=False)

    disciplines = relationship('Discipline', back_populates='teacher')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(255), nullable=False)
    group_id = Column('group_id', ForeignKey(Group.id, ondelete='CASCADE'), nullable=False)

    group = relationship(Group, back_populates='students')
    grades = relationship('Grade', back_populates='student')


class Discipline(Base):
    __tablename__ = 'disciplines'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete='CASCADE'), nullable=False)

    teacher = relationship(Teacher, back_populates='disciplines')
    grades = relationship('Grade', back_populates='discipline')


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    create_at = Column(DateTime, nullable=False)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete='CASCADE'), nullable=False)
    discipline_id = Column(Integer, ForeignKey(Discipline.id, ondelete='CASCADE'), nullable=False)

    student = relationship(Student, back_populates='grades')
    discipline = relationship(Discipline, back_populates='grades')