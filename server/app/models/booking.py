from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.db.base_class import Base

class BookingStatus(str, enum.Enum):
    UPCOMING = "upcoming"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    CANCELLED = "cancelled"

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    booking_code = Column(String, unique=True, index=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    duration_hours = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    payment_status = Column(String, default=PaymentStatus.PENDING)
    status = Column(String, default=BookingStatus.UPCOMING)
    created_at = Column(DateTime, default=datetime.now)

    user = relationship("User", backref="bookings", foreign_keys=[user_id])
    room = relationship("Room", backref="bookings", foreign_keys=[room_id])
    
    