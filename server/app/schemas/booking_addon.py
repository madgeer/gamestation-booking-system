from pydantic import BaseModel

class BookingAddonCreate(BaseModel):
    product_id: int
    quantity: int = 1

class BookingAddonResponse(BaseModel):
    id: int
    booking_id: int
    product_id: int
    quantity: int
    subtotal: float
    
    class Config:
        from_attributes = True