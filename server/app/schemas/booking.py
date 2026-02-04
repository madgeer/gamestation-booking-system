from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List
from app.schemas.booking_addon import BookingAddonResponse

class BookingBase(BaseModel):
    room_id: int
    start_time: datetime
    duration_hours: int
    

class BookingCreate(BaseModel):
    pass


class BookingResponse(BaseModel):
    id: int
    booking_code: str
    end_time: datetime
    total_price: float
    status: str

    class Config:
        from_attributes = True


class BookingDetail(BookingResponse):
    addons: List[BookingAddonResponse] = []


class BookingUpdateStatus(BaseModel):
    payment_status: str

class BookingReport(BaseModel):
    date: date
    total_bookings: int
    total_revenue: float
    bookings: List[BookingResponse]