from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingResponse
from app.crud import crud_booking
from app.schemas.booking_addon import BookingAddonCreate, BookingAddonResponse
from app.crud import crud_booking_addon

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
    
@router.post("/{booking_id}/addons", response_model=BookingAddonResponse)
def add_snack_to_booking(
    booking_id: int,
    addon_in: BookingAddonCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user)
):
    """
    User/Admin nambahin jajan ke booking tertentu.
    Otomatis update total harga booking.
    """
    return crud_booking_addon.create_booking_addon(db, booking_id, addon_in)