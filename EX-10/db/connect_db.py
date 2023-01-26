import configparser
import pathlib

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_DISCIPLINES = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 20

engine = create_engine("sqlite:///mynotes.db")
Session = sessionmaker(bind=engine)
session = Session()