from pydantic import BaseModel
from typing import List

class OrderDetailBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailResponse(OrderDetailBase):
    id: int

class OrderBase(BaseModel):
    customer_name: str
    customer_phone: str
    total_price: float
    status: str
    order_detail: List[OrderDetailCreate]

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: str | None = None
    customer_phone: str | None = None
    status: str | None = None
    order_detail: List[OrderDetailCreate] | None = None

class OrderResponse(OrderBase):
    id: int
    order_detail: List[OrderDetailResponse]

    class Config:
        from_attributes = True
