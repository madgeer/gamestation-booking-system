from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.booking import Booking
from app.models.product import Product
from app.models.booking_addon import BookingAddon
from app.schemas.booking_addon import BookingAddonCreate

def create_booking_addon(db: Session, booking_id: int, addon_in: BookingAddonCreate):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    
    product = db.query(Product).filter(Product.id == addon_in.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    
    subtotal = product.price * addon_in.quantity

    db_addon = BookingAddon(
        booking_id=booking_id,
        product_id=addon_in.product_id,
        quantity=addon_in.quantity,
        subtotal=subtotal
    )
    db.add(db_addon)
    
    booking.total_price += subtotal
    db.add(booking) 

    db.commit()
    db.refresh(db_addon)
    
    return db_addon