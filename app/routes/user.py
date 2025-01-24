from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.user import signup_user, login_user
from app.schemas.user import UserCreate, UserLogin, Token
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/signup", response_model=dict)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return signup_user(db, user.username, user.email, user.password)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user.username, user.password)
