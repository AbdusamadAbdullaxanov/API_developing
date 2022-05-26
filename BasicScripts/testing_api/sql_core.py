from sqlalchemy import MetaData, Column, String, Integer, Table
from sqlalchemy import create_engine
import sqlite3

meta = MetaData()
BASICCONNECTION = 'postgresql://postgres:postgresql@localhost/FastAPI'
engine = create_engine(BASICCONNECTION)
users = Table(
    'Students', meta,
    Column("id", Integer, primary_key=True),
    Column('txt', String, nullable=False)
)
meta.create_all(engine)


# tepadagi avvalgi narsala
def insert_data(txt: str = "default"):
    try:
        query = users.insert().values(txt=txt)
        connection = engine.connect()  # bu huddi  < connection = sqlite3.connect() >  ga o'xshaydi
        connection.execute(query)  # bu cursor.execute()  ga o'xshash
        return "inserted successfully"
    except Exception as e:
        return e


# def insert_data2(txt: str = 'default'):
#     l = [txt]
#     connection = sqlite3.connect("database.db")
#     cursor = connection.cursor()
#     cursor.execute("""INSERT INTO Users VALUES (?)""", l)
#     connection.commit()

def update_posts(id_num: int, text: str = ''):
    query = users.update().where(users.columns.id == id_num).values(txt=text)
    connection = engine.connect()
    connection.execute(query)


def delete_users(id_num: int):
    state = users.delete().where(users.columns.id == id_num)
    connection = engine.connect()
    connection.execute(state)
    return "deleted successfully"


def select(idnum: int):
    """SELECT * FROM users WHERE id = 5"""
    exe = users.select().where(users.c.id == idnum)
    connection = engine.connect()
    return connection.execute(exe).fetchone()


if __name__ == '__main__':
    print(insert_data())
    # print(select(3))
