from enum import unique
from sqlalchemy import Boolean, Column, Float, Integer, String
from . database import Base



class Address(Base):
    __tablename__= 'address'
    
    id = Column(Integer,primary_key=True, index=True)
    First_name = Column(String)
    Last_name = Column(String)
    Latitude = Column(Float)
    Longitude = Column(Float)