try:
    from .sqlalchemy_start import start, engine
except:
    from sqlalchemy_start import start, engine
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from datetime import datetime


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
    owner = Column(Integer, ForeignKey('Users.id', ondelete='CASCADE'), nullable=False)


class Votes(start):
    __tablename__ = "votes"

    user_id = Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(Integer, ForeignKey("Posts.id", ondelete="CASCADE"), primary_key=True)


# to create tables
def create_table():
    p = Posts_table()
    u = User_table()
    v = Votes()
    p.metadata.create_all(engine)
    u.metadata.create_all(engine)
    v.metadata.create_all(engine)


if __name__ == '__main__':
    create_table()
