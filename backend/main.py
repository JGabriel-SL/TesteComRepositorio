import models 
from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import Session 
from database import engine, SessionLocal
from models import Student

from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

class StudentRequest(BaseModel):
    id: int
    name: str
    email: str
    number: str
    registerr: str
    class_n: str
    school_shift: str

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:8000/register",
    "http://localhost:8000/student"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
async def hello_world():
    return {'Hello': 'World'}  

# CRUD

students = []

@app.post('/register/')
async def register_student(student_request: StudentRequest, db: Session = Depends(get_db)):
    try :
        print(student_request)
        student = Student()
        student.name = student_request.name
        student.email = student_request.email
        student.number = student_request.number
        student.register = student_request.registerr
        student.class_n = student_request.class_n
        student.school_shift = student_request.school_shift
        db.add(student)
        db.commit()
        return {
            "code" : "sucess",
            "student": student
        }  
    except: 
        return {"error": "not connection"}

@app.get('/student/')
async def getAll_students(db: Session = Depends(get_db)):

    try:
        student = Student
        studen = db.query(student).all()
        return studen
    except:
        return{
            "error": "not connection"
        }

@app.get('/student/{id}')
async def get_student(id: int, db: Session = Depends(get_db)):
    try:
        student = Student
        print(id)
        studen = db.query(student).filter_by(id=id).first()
        return studen
    except:
        raise HTTPException(status_code=404, detail="Student Not Found")

@app.put('/student/{id}')
async def update_student(id: int, student_request: StudentRequest, db: Session = Depends(get_db)):
    try:
        student = Student
        studentAux = db.query(student).filter_by(id=id).first()
        studentAux.name = student_request.name
        studentAux.email = student_request.email
        studentAux.number = student_request.number
        studentAux.register = student_request.registerr
        studentAux.class_n = student_request.class_n
        studentAux.school_shift = student_request.school_shift
        db.commit()
        return studentAux
    except:
        raise HTTPException(status_code=404, detail="Student Not Found")

@app.delete('/student/{id}')
async def delete_student(id: int, db: Session = Depends(get_db)):
    try:
        student = Student
        print(id)
        studen = db.query(student).filter_by(id=id).first()
        print(studen)
        db.delete(studen)
        db.commit()
        return {"teste": "ok"}
    except:
        return{
            "error": "not connection"
        }
        