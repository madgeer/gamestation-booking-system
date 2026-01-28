from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingResponse
from app.crud import crud_booking

router = APIRouter()

@router.post("/", response_model=BookingResponse)
def create_new_booking(
    booking_in: BookingCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    try:
        booking = crud_booking.create_booking(
            db=db, 
            booking_in=booking_in, 
            user_id=current_user.id
        )
        return booking
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))