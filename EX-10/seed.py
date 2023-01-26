from seeds import groups, teachers, students, disciplines, grades

if __name__ == '__main__':
    groups.create_groups()
    teachers.create_teachers()
    students.create_students()
    disciplines.create_disciplines()
    grades.create_grades()