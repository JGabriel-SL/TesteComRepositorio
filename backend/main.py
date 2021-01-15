from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

class Student(BaseModel):
    name: str
    email: str
    number: str
    registration: str
    class_number: str
    school_shift: str

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'Hello': 'World'}  

# CRUD

students = []

@app.post('/register')
async def register_student(student: Student):
    students.append(student)
    return student

@app.get('/student', response_model=List[Student])
async def getAll_students():
    return students

@app.get('/student/{id}')
async def get_student(id: int):
    try:
        return students[id]
    except:
        raise HTTPException(status_code=404, detail="Student Not Found")

@app.put('/student/{id}')
async def update_student(id: int, student: Student):
    try:
        students[id] = student
        return student
    except:
        raise HTTPException(status_code=404, detail="Student Not Found")

@app.delete('/student/{id}')
async def delete_student(id: int):
    try:
        obj = students[i]
        students.pop(i)
        return obj
    except:
        raise HTTPException(status_code=404, detail="Student Not Found")
        