from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Enum
from sqlalchemy.sql import func
from app.db.base_class import Base
import enum

class UserRole(str, enum.Enum):
    CUSTOMER = "customer"
    ADMIN = "admin"
    STAFF = "staff"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    phone_number = Column(String)
    role = Column(Enum(UserRole))
    avatar_url = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())