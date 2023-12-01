from fastapi import APIRouter

from database.studentservice import register_new_student_db, delete_student_db, edit_student_db, get_exact_student_db, check_student_email_db

from student import StudentRegisterValidator, EditStudentValidator

students_router = APIRouter(prefix='/student', tags=['Работа со студентами'])


# Регистрация
@students_router.post('/register')
async def register_student(data: StudentRegisterValidator):
    # Переводим pydantic в обычный словарь
    new_student_data = data.model_dump()
    # {'name':'asd'}

# вызов функции для проверки почты в базе
    checker = check_student_email_db(data.email)
    if not checker:
        result = register_new_student_db(**new_student_data)
        return {'message': result}

    return {'message': 'Студент с такой почтой уже есть в БД'}


# Получения инфы о студенте
@students_router.get('/info')
async def get_student(student_id: int):
    result = get_exact_student_db(student_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}


# Изменить данные о студенте
@students_router.put('/edit-data')
async def edit_student(data: EditStudentValidator):
    change_data = data.model_dump()

    result = edit_student_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}


# Удаление студента из базы данных
@students_router.delete('/delete-student')
async def delete_user(student_id: int):
    result = delete_student_db(student_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ничего не найдено'}
