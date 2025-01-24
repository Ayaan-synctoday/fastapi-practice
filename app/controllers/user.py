from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.utils.auth import get_password_hash, verify_password, create_access_token
from datetime import timedelta

def signup_user(db: Session, username: str, email: str, password: str):
    db_user = db.query(User).filter((User.username == username) | (User.email == email)).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(password)
    new_user = User(username=username, email=email,phone=phone , hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
