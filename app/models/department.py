from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base



class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key= True, index= True)
    name = Column(String(600),unique=True, nullable= False,)

