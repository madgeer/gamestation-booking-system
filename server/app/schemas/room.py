from pydantic import BaseModel
from typing import Optional

class RoomBase(BaseModel):
    name: str
    type: str = "Regular" # VIP, Regular, RacingSim
    console_type: str     # PS5, PS4
    price_per_hour: float
    facilities: Optional[str] = None

class RoomCreate(RoomBase):
    gamestation_id: int  # Pas bikin room, wajib sebutin ini room cabang mana

class RoomResponse(RoomBase):
    id: int
    gamestation_id: int
    status: str
    is_currently_booked: bool = False

    class Config:
        from_attributes = True