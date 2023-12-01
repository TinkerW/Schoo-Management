from fastapi import FastAPI

from student.student_api import students_router
from teacher.teacher_api import teacher_router
from mark.mark_api import mark_router
# from mark.mark_api import mark_router

# Создать базу
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(students_router)
app.include_router(teacher_router)
app.include_router(mark_router)
