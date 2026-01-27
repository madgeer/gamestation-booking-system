from sqlalchemy import Column, Integer, String, Boolean, Float, Text, Time
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class GameStation(Base):
    __tablename__ = "gamestations"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True, nullable=False)
    address = Column(Text, nullable=True)
    city = Column(String, index=True)

    open_hour = Column(Time, nullable=True)
    close_hour = Column(Time, nullable=True)
    is_active = Column(Boolean, default=True)

    rooms = relationship("Room", back_populates="gamestation")

    