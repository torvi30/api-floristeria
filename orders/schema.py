from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    customer_name: str
    customer_phone: str
    total_price: float
    status: str = "pendiente"

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int

    class Config:
        from_attributes = True
