from sqlalchemy_ORM import Session, TAble
from fastapi import HTTPException, status
from fastapi import FastAPI

app = FastAPI()


@app.get("/search")
def search_item(num: int = 0):
    # _____________________HAVE_NO_PROBLEMS____WORKING_PROPERLY_____________________________________________________
    session = Session()
    session.begin()
    back = session.query(TAble).all()
    if back is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found data')
    return back


def insert(word: str | None = None):
    obj = TAble(word=word)
    cursor = Session()
    cursor.add(obj)
    cursor.commit()


def search(id_number: int):
    cursor = Session()
    ret = cursor.query(TAble).filter(TAble.id == 1).first()
    return ret


def update(id: int, word: str):
    cursor = Session()
    item = cursor.query(TAble).filter(TAble.id == id).first()
    item.word = word
    cursor.commit()


if __name__ == '__main__':
    print(search_item())
