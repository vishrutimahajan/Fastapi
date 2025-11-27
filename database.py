from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


dburl = "postgresql://postgres:root%40123@localhost:5432/vishruti"  #database url for connecting to the database
engine = create_engine(dburl)    #create_engine is used to create a new SQLAlchemy engine instance
Sessionlocal = sessionmaker(autoflush= False , autocommit = False, bind = engine ) #autoflush and autocommit are set to false to avoid unwanted changes to the database and bind is used to bind the engine to the session
