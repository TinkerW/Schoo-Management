# NOT FULL

from pydantic import BaseModel


class TeacherRegisterValidator(BaseModel):
    name: str
    surname: str
    subject_name: str
    school_number: str
    phone_number: str
    email: str
    password: str


class EditTeacherValidator(BaseModel):
    teacher_id: int
    edit_type: str
    new_data: str
