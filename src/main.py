from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Student Management API")


class Student(BaseModel):
    id: int
    name: str
    department: str
    semester: int
    cgpa: float


students = [
    Student(
        id=1,
        name="Murad Hasan",
        department="CSE",
        semester=4,
        cgpa=3.50
    ),
    Student(
        id=2,
        name="Badhon Ahmed",
        department="CSE",
        semester=4,
        cgpa=3.70
    )
]


# GET - Get all students
@app.get("/students")
def get_students():
    return students


# GET - Get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# POST - Add a new student
@app.post("/students", status_code=201)
def create_student(student: Student):
    for existing_student in students:
        if existing_student.id == student.id:
            raise HTTPException(
                status_code=400,
                detail="Student ID already exists"
            )

    students.append(student)

    return student


# PUT - Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id and updated_student.id == student_id:
            students[index] = updated_student
            return updated_student

    raise HTTPException(
        status_code=404,
        detail="Student not found or student ID mismatch"
    )


# DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted_student = students.pop(index)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )