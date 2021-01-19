from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    number = Column(String, index=True)
    register = Column(String, index=True)
    class_n = Column(String, index=True)
    school_shift = Column(String, index=True)
