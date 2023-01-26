from faker import Faker
import random

from db.connect_db import session, NUMBER_STUDENTS
from db.models import Student, Group

fake = Faker('uk_UA')


def create_students():
    groups = session.query(Group).all()

    for _ in range(NUMBER_STUDENTS):
        group = random.choice(groups)

        student = Student(
            fullname=fake.name(),
            group_id=group.id
        )
        session.add(student)

    session.commit()


if __name__ == '__main__':
    create_students()