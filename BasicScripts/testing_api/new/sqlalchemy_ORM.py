from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, String, Integer

CONNECTION = "postgresql://postgres:postgresql@localhost/FastAPI"

engine = create_engine(CONNECTION)  # connection = sqlite3.connect("base.db")
Session = sessionmaker(bind=engine)  # cursor = connection.cursor()
Base = declarative_base()  # CREATE TABLE IF NOT EXISTS ()


class TAble(Base):
    __tablename__ = "newtable"

    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)


create = TAble()
create.metadata.create_all(engine)
