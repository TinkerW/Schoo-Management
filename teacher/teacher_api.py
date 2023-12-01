# NOT FULL

from fastapi import APIRouter

from database.teacherservice import register_new_teacher_db, delete_teacher_db, edit_teacher_db, get_exact_teacher_db, check_teacher_email_db

from teacher import TeacherRegisterValidator, EditTeacherValidator

teacher_router = APIRouter(prefix='/teacher', tags=['Работа с учителями'])


# Регистрация
@teacher_router.post('/register')
async def register_teacher(data: TeacherRegisterValidator):
    # Переводим pydantic в обычный словарь
    new_teacher_data = data.model_dump()
    # {'name':'asd'}

# вызов функции для проверки почты в базе
    checker = check_teacher_email_db(data.email)
    if not checker:
        result = register_new_teacher_db(**new_teacher_data)
        return {'message': result}

    return {'message': 'Уже имеется'}


# Получение инфы об учителе
@teacher_router.get('/info')
async def get_teacher(teacher_id: int):
    result = get_exact_teacher_db(teacher_id)

    if result:
        return {'message': result}
    else:
        return {'message':  "Ничего не найдено"}


# Изменить данные об учителе
@teacher_router.put('/edit-data')
async def edit_teacher(data: EditTeacherValidator):
    change_data = data.model_dump()

    result = edit_teacher_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}


# Удаление учителя из базы данных
@teacher_router.delete('/delete-teacher')
async def delete_teacher(teacher_id: int):
    result = delete_teacher_db(teacher_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Нет учителя на увольнение('}
