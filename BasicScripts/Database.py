from sqlalchemy_start import Session
from models import User_table, create_table, Posts_table
from utils import hash_pssd, verify_password
from Oauth2 import get_current_user, access_token, COPY
from fastapi import HTTPException, status
import models as mode
from fastapi.security import OAuth2PasswordBearer

s = OAuth2PasswordBearer(tokenUrl="vote")
tokenn = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InZvdGluZzJAZ21haWwuY29tIiwicGFzc3dvcmQiOiIyMDA1MTIwNSIsImV4cCI6MTY1MzQzODcyM30.uM1oi6R1Kru-pAaHXpujP0XnKQA_sl14cMKCaAIB6ck"


class Function:
    def __init__(self):
        create_table()
        self.session = Session()

    def signup(self, mail: str, password: str):
        hashed = hash_pssd(password)
        account = User_table(mail=mail, password=str(hashed))
        data = {"email": account.mail, "password": password}
        self.session.begin()
        self.session.add(account)
        self.session.commit()
        return access_token(data)

    def verify_acount(self, token: str):
        try:
            decoded2 = get_current_user(token)
            self.session.begin()
            back = self.session.query(User_table).filter(User_table.mail == decoded2.get("mail"),
                                                         User_table.password == decoded2.get('password'))
            if back.first() is None:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not signed up')
            return back.first()
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(error))

    def verify(self, mail: str, password: str):
        user = self.session.query(User_table.mail, User_table.password).filter(
            User_table.mail == mail).first()
        print("user " + str(user))
        if user is not None and verify_password(user[1], password):
            return True


class Create_Posts(Function):

    def get_all_posts(self, limit: int = 10, skip: int = 0):
        self.session.begin()
        fill = self.session.query(Posts_table).offset(skip).limit(limit).all()
        return fill

    def insert_data(self, data: dict):
        try:
            number = self.session.query(User_table.id).filter(User_table.mail == "Abdusamad_python@gmail.com").first()
            insert = Posts_table(owner=int(number[0]), **data)
            self.session.begin()
            self.session.add(insert)
            self.session.commit()
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail='inserted data')
        except Exception as error:
            print("---->  " + str(error))

    def search(self, num: int):
        # _____________________HAVE_NO_PROBLEMS____WORKING_PROPERLY_____________________________________________________
        self.session.begin()
        back = self.session.query(Posts_table).filter(Posts_table.id == num)
        if back.first() is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Not found data')
        print(back.first())
        return back.first()

    def update_posts(self, id_number: int, dictdata: dict | None = None):
        try:
            update = self.session.query(Posts_table).get(id_number)
            update.title, update.content, update.published = dictdata.get("title"), dictdata.get(
                "content"), dictdata.get("published")
            raise HTTPException(status_code=status.HTTP_201_CREATED, detail="Your post is successfully updated!")
        except Exception as error:
            return {"Internal server error": str(error)}

    def delete_post(self, id_num: int):
        # _____________________HAVE_NO_PROBLEMS____WORKING_PROPERLY_____________________________________________________
        check = self.session.query(Posts_table).filter(Posts_table.id == id_num).first()
        self.session.query(Posts_table).filter(Posts_table.id == id_num).delete(synchronize_session=False)
        if check is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Id with {id_num} not found')
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)


class Voting:
    def __init__(self):
        self.session = Session()
        create_table()

    def vote_posts(self, post_id: int, boolean: int):
        global tokenn
        self.session.begin()
        user = get_current_user(tokenn).get("email")
        user_id = self.session.query(User_table.id).filter(User_table.mail == user).first()[0]
        post_from_base = self.session.query(Posts_table).filter(Posts_table.id == post_id).first()
        find_vote = self.session.query(mode.Votes).filter(mode.Votes.post_id == post_id,
                                                          mode.Votes.user_id == int(user_id)).first()
        if boolean == 1:
            if post_from_base is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with {post_id} does not exist')
            if find_vote is not None:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                    detail=f'You already liked this post: {post_id}')
            insert = mode.Votes(post_id=post_id, user_id=int(user_id))
            self.session.add(insert)
            self.session.commit()
        else:
            self.session.query(mode.Votes).filter(mode.Votes.post_id == post_id).delete(synchronize_session=False)
            self.session.commit()
            return {"message": "undone your vote"}


if __name__ == '__main__':
    add = Function()
    pr = {"mail": 'pythondeveloper441@gmail.com',
          "password": '$2b$12$qW3lUxEosBQ4fxGdTRAjwO0HN2I6obKBo6wDTAEi/YshszoRAjncS'}
    print(COPY)
