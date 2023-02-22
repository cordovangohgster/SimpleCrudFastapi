from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+mysqlconnector://root@localhost/simplepythoncrud'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()