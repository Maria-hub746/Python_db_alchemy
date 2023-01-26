from faker import Faker
import random

from db.connect_db import session, NUMBER_DISCIPLINES
from db.models import Discipline, Teacher

fake = Faker('uk_UA')


def create_subjects():
    teachers = session.query(Teacher).all()

    for _ in range(NUMBER_DISCIPLINES):
        teacher = random.choice(teachers)

        discipline = Discipline(
            name=fake.job(),
            teacher_id=teacher.id
        )
        session.add(discipline)

    session.commit()


if __name__ == '__main__':
    create_disciplines()