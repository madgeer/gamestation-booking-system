from sqlalchemy import Column, Integer, String, Float, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

class ProductCategory(str, enum.Enum):
    EQUIPMENT = "equipment" # Stik tambahan, Converter, dll
    FOOD = "food"           # Indomie, Snack
    BEVERAGE = "beverage"   # Kopi, Nutrisari

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)   # Misal: "Indomie Goreng"
    category = Column(String, nullable=False) 
    price = Column(Float, nullable=False)   # Misal: 5000.0
    image_url = Column(String, nullable=True)
    
    # Relasi ke booking_addons (Nanti)
    booking_addons = relationship("BookingAddon", back_populates="product")