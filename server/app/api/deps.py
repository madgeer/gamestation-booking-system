# Dependencies (misal: get_current_user, get_db)
from typing import Generator
from app.db.sessions import SessionLocal
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core import security
from app.db.sessions import SessionLocal
from app.models.user import User
from app.crud import crud_user
from app.schemas.token import TokenPayLoad

# setup database
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()

# setup penjaga token
reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)

def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(reusable_oauth2)
) -> User:
    """
    Fungsi ini akan dipanggil di setiap endpoint yang butuh login.
    Tugasnya: Baca Token -> Cari Usernya di DB -> Kembalikan Data User.
    """
    try:
        # Decode Token
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = TokenPayLoad(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    
    # Cari user di DB berdasarkan ID yang ada di token
    user = crud_user.get_user_by_id(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user