from sqlalchemy.orm  import Session
from sqlalchemy import and_
from datetime import timedelta
import uuid

from sqlalchemy.orm import Session
from app.models.booking import Booking, BookingStatus
from app.models.room import Room
from app.schemas.booking import BookingCreate

def check_availability(db: Session, room_id: int, start_time, end_time):
    overlap = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.status != BookingStatus.CANCELLED,
        and_(
            Booking.start_time < end_time,
            Booking.end_time > start_time
        )
    ).first()

    if overlap:
        return False
    return True

def create_booking(db: Session, booking_in: BookingCreate, user_id: int):
    end_time = booking_in.start_time + timedelta(hours=booking_in.duration_hours)
    
    room = db.query(Room).filter(Room.id == booking_in.room_id).first()
    if not room:
        raise ValueError("Room not found")

    
    is_available = check_availability(db, room.id, booking_in.start_time, end_time)
    if not is_available:
        raise ValueError("Room is already booked at this time")

    
    total_price = room.price_per_hour * booking_in.duration_hours
    
    code = f"GS-{uuid.uuid4().hex[:8].upper()}"

    db_booking = Booking(
        user_id=user_id,
        room_id=booking_in.room_id,
        booking_code=code,
        start_time=booking_in.start_time,
        end_time=end_time,
        duration_hours=booking_in.duration_hours,
        total_price=total_price,
        status=BookingStatus.UPCOMING
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking