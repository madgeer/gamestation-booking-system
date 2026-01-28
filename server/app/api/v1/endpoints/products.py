from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.api import deps
from app.models.user import User
from app.schemas.product import ProductCreate, ProductResponse
from app.crud import crud_product

router = APIRouter()

@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(deps.get_db)):
    return crud_product.get_products(db)

@router.post("/", response_model=ProductResponse)
def create_product(
    product_in: ProductCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user) # Cuma Admin/User Login yang boleh nambah menu
):
    return crud_product.create_product(db, product_in)