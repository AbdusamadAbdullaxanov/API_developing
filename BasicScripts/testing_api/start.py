from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from datetime import datetime

BASICCONNECTION = 'postgresql://postgres:postgresql@localhost/FastAPI'
engine = create_engine(BASICCONNECTION)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=True)
start = declarative_base()


# table for user account
class User_table(start):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, nullable=False)
    mail = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(String, nullable=False, default=str(datetime.now()))


# table for posts that user created
class Posts_table(start):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True, nullable=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, default=False)

    owner = Column(Integer, ForeignKey("Users.id", ondelete='CASCADE'), nullable=False)


if __name__ == '__main__':
    a = Posts_table()
    a.metadata.create_all(engine)
    b = Posts_table()
    b.metadata.create_all(engine)
