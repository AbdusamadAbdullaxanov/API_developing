from fastapi import APIRouter, Depends, HTTPException, status
from Validation import Votes
from Oauth2 import get_current_user
from Database import Voting

router = APIRouter(
    prefix='/vote'
)


@router.post("/")
def votes(payload: Votes):
    like = Voting()
    return like.vote_posts(payload.post_id, payload.like)
# , current_user: dict = Depends(get_current_user)
