from fastapi import APIRouter
from database.markservice import add_mark_db, edit_mark_db

mark_router = APIRouter(prefix='/card', tags=['Выставление оценок'])


@mark_router.post('/add-mark')
async def add_mark(user_id: int, sub_name: str, sub_mark: int):
    result = add_mark_db(user_id, sub_name, sub_mark)

    return result


@mark_router.post('/edit-mark')
async def edit_mark(sub_id: int, new_mark: int):
    result = edit_mark_db(sub_id, new_mark)

    return result


