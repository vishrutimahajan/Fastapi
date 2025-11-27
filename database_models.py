
from sqlalchemy import Column, Integer, String, Float # Importing necessary modules from SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base # Importing the declarative base for SQLAlchemy models 
#declative base is used to create classes that define the structure of database tables.

Base = declarative_base() # Base class for all database models

class Product(Base):

    __tablename__ = 'product'  # Name of the table in the database

    id = Column(Integer, primary_key= True)
    name= Column(String(60))
    description=Column(String)
    price= Column(Float)
    quantity= Column(Integer)