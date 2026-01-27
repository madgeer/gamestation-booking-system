from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.models.user import User

from app.schemas.gamestation import GameStationCreate, GameStationResponse
from app.schemas.room import RoomCreate, RoomResponse

from app.crud import crud_gamestation, crud_room

router = APIRouter()

@router.get("/", response_model=List[GameStationResponse])
def read_gamestations(db: Session = Depends(deps.get_db)):
    return crud_gamestation.get_gamestations(db)

@router.post("/", response_model=GameStationResponse)
def create_gamestation(
    station_in: GameStationCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user) # Wajib Login
):
    return crud_gamestation.create_gamestation(db, station_in)



@router.post("/rooms", response_model=RoomResponse)
def create_room(
    room_in: RoomCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user) # Wajib Login
):
    
    return crud_room.create_room(db, room_in)

@router.get("/{gamestation_id}/rooms", response_model=List[RoomResponse])
def read_rooms_by_location(
    gamestation_id: int,
    db: Session = Depends(deps.get_db)
):
    return crud_room.get_rooms_by_gamestation(db, gamestation_id)