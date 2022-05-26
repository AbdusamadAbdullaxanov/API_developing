from fastapi import APIRouter, status, Depends, HTTPException
from Validation import CreatePosts, UpdatePosts
from Database import Create_Posts
from Oauth2 import get_current_user

router = APIRouter()


@router.get("/posts")
def all_posts(limit: int = 10, skip: int = 0):
    posts = Create_Posts()
    return posts.get_all_posts(limit=limit, skip=skip)


@router.post("/create")
def create_posts(post: CreatePosts, user_id: dict = Depends(get_current_user)):
    add = Create_Posts()
    hardcode = {"mail": user_id.get("email"), "password": user_id.get("password")}
    # if add.verify(hardcode):
    return add.insert_data(post.dict())


@router.get('/search/{num}', status_code=status.HTTP_200_OK)
def search_posts(num: int = 0, user_id: dict = Depends(get_current_user)):
    post = Create_Posts()
    hardcode = {"mail": user_id.get("email"), "password": user_id.get("password")}
    # if post.verify(hardcode):
    return post.search(num)
    # print("user_id  " + str(user_id))


@router.put("/update{idd}")
def update_posts(idd: int, body: UpdatePosts, user: dict = Depends(get_current_user)):
    updater = Create_Posts()
    hardcode = {"mail": user.get("email"), "password": user.get("password")}
    # if updater.verify(hardcode):
    return updater.update_posts(idd, body.dict())


@router.delete("/delete/{post_id}")
def delete_posts(post_id: int, user_id: dict = Depends(get_current_user)):
    post = Create_Posts()
    hardcode = {"mail": user_id.get("email"), "password": user_id.get("password")}
    # if post.verify(hardcode):
    post.delete_post(post_id)
    # else:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Unauthorized Account')
