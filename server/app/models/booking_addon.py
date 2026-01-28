from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class BookingAddon(Base):
    __tablename__ = "booking_addons"

    id = Column(Integer, primary_key=True, index=True)
    
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    quantity = Column(Integer, default=1)
    subtotal = Column(Float, nullable=False) 

    # Relasi
    booking = relationship("Booking", backref="addons")
    product = relationship("Product", back_populates="booking_addons")