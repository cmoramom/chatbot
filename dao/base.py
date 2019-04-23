# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///chatroom.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
Base = declarative_base()
