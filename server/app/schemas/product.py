from pydantic import BaseModel
from typing import Optional
from app.models.product import ProductCategory

class ProductBase(BaseModel):
    name: str
    category: ProductCategory 
    price: float
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True