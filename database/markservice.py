from database import get_db
from database.models import Subject


def add_mark_db(user_id, subject_name, subject_mark):
    db = next(get_db())

    new_obj = Subject(user_id=user_id, subject_name=subject_name, subject_mark=subject_mark)

    db.add(new_obj)
    db.commit()

    return f'Оценка к предмету добавлена id - {new_obj.subject_id}'


def edit_mark_db(sub_id, new_mark):
    db = next(get_db())

    cheker = db.query(Subject).filter_by(subject_id=sub_id).first()

    if cheker:
        cheker.subject_order = new_mark

        db.commit()

    return 'Оценка изменена'

