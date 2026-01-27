from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
import enum

# Definisi Enum biar sama kayak SQL
class RoomType(str, enum.Enum):
    VIP = "VIP"
    REGULAR = "Regular"
    RACING = "RacingSim"

class RoomStatus(str, enum.Enum):
    AVAILABLE = "available"
    MAINTENANCE = "maintenance"

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    gamestation_id = Column(Integer, ForeignKey("gamestations.id"), nullable=False)
    
    name = Column(String, nullable=False)       # Misal: "Room 01"
    type = Column(String, default=RoomType.REGULAR) # Simpan sebagai string di DB
    console_type = Column(String)               # Misal: "PS5"
    price_per_hour = Column(Float, nullable=False)
    facilities = Column(Text, nullable=True)
    status = Column(String, default=RoomStatus.AVAILABLE)

    # Relasi balik ke Cabang
    gamestation = relationship("GameStation", back_populates="rooms")