#!/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
        "mysql+pymysql://root:password@172.17.0.8/test?host=172.17.0.6?port=3306")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __table__ = Table('user', Base.metadata, autoload=True, autoload_with=engine)

    def __str__(self):
        return '' + self.first_name + ' ' + self.last_name


for x in range(0, 100000):
    user = User(first_name='Alberto', last_name='Ochoa')
    session.add(user)
    session.flush()



print(session.query(User).count())
session.query(User).all()
session.commit()
