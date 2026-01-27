from sqlalchemy.orm import Session
from app.models.room import Room
from app.schemas.room import RoomCreate

def get_rooms_by_gamestation(db: Session, gamestation_id: int):
    return db.query(Room).filter(Room.gamestation_id == gamestation_id).all()

def create_room(db: Session, room: RoomCreate):
    db_room = Room(
        gamestation_id=room.gamestation_id,
        name=room.name,
        type=room.type,
        console_type=room.console_type,
        price_per_hour=room.price_per_hour,
        facilities=room.facilities
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room