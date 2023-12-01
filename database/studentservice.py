# FULL
from datetime import datetime

from database.models import Student
from database import get_db



# Регистрация студента (name, surname, class_number, school_number, phone_number, email, password)
def register_new_student_db(name, surname, class_number, school_number,
                            phone_number, email, password):
    db = next(get_db())

    new_student = Student(name=name, surname=surname, class_number=class_number, school_number=school_number,
                    phone_number=phone_number, email=email, password=password,
                    reg_date=datetime.now())
    db.add(new_student)
    db.commit()

    return f'id -{new_student.student_id}, name - {new_student.name}, mail - {new_student.email}'


# Получить инфо о студенте
def get_exact_student_db(student_id):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    return exact_student


# Проверка данных через (id)
def check_student_email_db(student_id):
    db = next(get_db())

    checker = db.query(Student).filter_by(student_id=student_id).first()

    if checker:
        return checker
    else:
        return False


# Изменить данные у студента/ Перевести его в другой класс
def edit_student_db(student_id, edit_type, new_data):
    db = next(get_db())

    exact_student = db.query(Student).filter_by(student_id=student_id).first()

    if exact_student:
        if edit_type == 'email':
            exact_student.email = new_data
        elif edit_type == 'password':
            exact_student.password = new_data
        elif edit_type == 'phone_number':
            exact_student = phone_number = new_data
        elif edit_type == 'class_number':
            exact_student = class_number = new_data

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Студент не найден'


# Удаления студента (student_id)
def delete_student_db(student_id):
    db = next(get_db())

    delete_student = db.query(Student).filter_by(student_id=student_id).first()

    if delete_student:
        db.delete(delete_student)
        db.commit()

        return 'Студент успешно удален'
    else:
        return 'Студент не найден'