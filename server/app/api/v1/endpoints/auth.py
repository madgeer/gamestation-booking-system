from typing import Any
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api import deps
from app.core import security
from app.crud import crud_user
from app.schemas.token import Token

router = APIRouter()

@router.post("/login/access-token", response_model=Token)
def login_access_token(
    db: Session = Depends(deps.get_db),
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = crud_user.get_user_by_email(db, email=form_data.username)

    if not user or not security.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail= "Incorect email or password")
    
    access_token_expires = security.create_access_token(subject=user.id)   

    return {
        "access_token": access_token_expires,
        "token_type": "bearer",
    } 
    