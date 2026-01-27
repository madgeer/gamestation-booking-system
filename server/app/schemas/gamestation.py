from pydantic import BaseModel
from typing import Optional
from datetime import time

class GameStationBase(BaseModel):
    name: str
    address: Optional[str] = None
    city: Optional[str] = None
    open_hour: Optional[time] = None
    close_hour: Optional[time] = None

class GameStationCreate(GameStationBase):
    pass

class GameStationResponse(GameStationBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True