from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    image: str
    type: str
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
