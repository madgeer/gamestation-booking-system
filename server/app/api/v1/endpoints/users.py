from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.schemas.user import UserCreate, UserResponse
from app.crud import crud_user

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_new_user(user_in: UserCreate, db: Session = Depends(deps.get_db)):
    """
    Register user baru
    """

    user =crud_user.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user = crud_user.create_user(db, user=user_in)
    return user
