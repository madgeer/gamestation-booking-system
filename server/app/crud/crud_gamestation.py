from sqlalchemy.orm import Session
from app.models.gamestation import GameStation
from app.schemas.gamestation import GameStationCreate

def get_gamestations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(GameStation).offset(skip).limit(limit).all()

def create_gamestation(db: Session, station: GameStationCreate):
    db_station = GameStation(
        name=station.name,
        address=station.address,
        city=station.city,
        open_hour=station.open_hour,
        close_hour=station.close_hour
    )
    db.add(db_station)
    db.commit()
    db.refresh(db_station)
    return db_station