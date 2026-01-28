from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BookingCreate(BaseModel):
    room_id: int
    start_time: datetime
    duration_hours: int

class BookingResponse(BaseModel):
    id: int
    booking_code: str
    room_id: int
    start_time: datetime
    end_time: datetime
    total_price: float
    status: str

    class Config:
        from_attributes = True