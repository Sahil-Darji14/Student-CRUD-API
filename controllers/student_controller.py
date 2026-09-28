from fastapi import HTTPException
from models.student_model import StudentCreate


students = []

next_id = 1


def create_student(student: StudentCreate):
    global next_id

    new_student = {
        "id": next_id,
        "name": student.name,
        "email": student.email,
        "course": student.course,
        "semester": student.semester
    }

    students.append(new_student)
    next_id += 1

    return new_student


def get_all_students():
    return students


def get_student_by_id(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def update_student(student_id: int, student: StudentCreate):
    for existing_student in students:
        if existing_student["id"] == student_id:

            existing_student["name"] = student.name
            existing_student["email"] = student.email
            existing_student["course"] = student.course
            existing_student["semester"] = student.semester

            return existing_student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )