# FULL

from pydantic import BaseModel


class StudentRegisterValidator(BaseModel):
    name: str
    surname: str
    class_number: str
    school_number: str
    phone_number: str
    email: str
    password: str


class EditStudentValidator(BaseModel):
    student_id: int
    edit_type: str
    new_data: str
