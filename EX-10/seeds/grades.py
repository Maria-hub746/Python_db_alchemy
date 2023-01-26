from datetime import datetime
from faker import Faker
import random

from db.connect_db import session, NUMBER_GRADES
from db.models import Grade, Student, Discipline

fake = Faker('uk_UA')


def create_grades():
    students = session.query(Student).all()
    disciplines = session.query(Discipline).all()

    for student in students:
        for _ in range(NUMBER_GRADES):
            discipline = random.choice(disciplines)
            grade = Grade(
                grade=random.randint(4, 12),
                create_at=fake.date_between_dates(datetime(2022, 9, 1), datetime(2022, 12, 31)),
                student_id=student.id,
                discipline_id=discipline.id
            )
            session.add(grade)

    session.commit()


if __name__ == '__main__':
    create_grades()