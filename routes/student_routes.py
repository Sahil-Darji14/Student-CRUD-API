
from fastapi import APIRouter, status
from typing import List

from models.student_model import StudentCreate, StudentResponse
from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)


router = APIRouter()


@router.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student_api(student: StudentCreate):
    return create_student(student)


@router.get(
    "/students",
    response_model=List[StudentResponse]
)
def get_all_students_api():
    return get_all_students()


@router.get(
    "/students/{id}",
    response_model=StudentResponse
)
def get_student_api(id: int):
    return get_student_by_id(id)


@router.put(
    "/students/{id}",
    response_model=StudentResponse
)
def update_student_api(id: int, student: StudentCreate):
    return update_student(id, student)


@router.delete(
    "/students/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_student_api(id: int):
    delete_student(id)