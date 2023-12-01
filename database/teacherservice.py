# NOT FULL
from datetime import datetime

from database.models import Teacher
from database import get_db



# Регистрация учителя (name, surname, subject_name, school_number, phone_number, email, password)
def register_new_teacher_db(name, surname, subject_name, school_number,
                            phone_number, email, password):
    db = next(get_db())

    new_teacher = Teacher(name=name, surname=surname, subject_name=subject_name, school_number=school_number,
                    phone_number=phone_number, email=email, password=password,
                    reg_date=datetime.now())
    db.add(new_teacher)
    db.commit()

    return f'id -{new_teacher.student_id}, name - {new_teacher.name}, mail - {new_teacher.email}'


# Получить инфу об учителе
def get_exact_teacher_db(teacher_id):
    db = next(get_db())

    exact_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    return exact_teacher


# Проверка данных через (id)
def check_teacher_email_db(teacher_id):
    db = next(get_db())

    checker = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if checker:
        return checker
    else:
        return False


# Изменить данные об учителе
def edit_teacher_db(teacher_id, edit_type, new_data):
    db = next(get_db())

    exact_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if exact_teacher:
        if edit_type == 'email':
            exact_teacher.email = new_data
        elif edit_type == 'password':
            exact_teacher.password = new_data
        elif edit_type == 'phone_number':
            exact_teacher = phone_number = new_data

        db.commit()

        return 'Данные изменены'
    else:
        return 'Не найдено'


# Уволить ко всем чертям учителя
def delete_teacher_db(teacher_id):
    db = next(get_db())

    delete_teacher = db.query(Teacher).filter_by(teacher_id=teacher_id).first()

    if delete_teacher:
        db.delete(delete_teacher)
        db.commit()

        return "Удалено"
    else:
        return 'Не найдено'