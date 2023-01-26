from faker import Faker

from db.connect_db import session, NUMBER_TEACHERS
from db.models import Teacher

fake = Faker('uk_UA')


def create_teachers():
    for _ in range(NUMBER_TEACHERS):
        teacher = Teacher(
            fullname=fake.name(),

        )
        session.add(teacher)

    session.commit()


if __name__ == '__main__':
    create_teachers()