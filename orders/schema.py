from pydantic import BaseModel
from typing import List, Optional

# Schemas para OrderDetail
class OrderDetailBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailResponse(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True

# Schemas para Order
class OrderBase(BaseModel):
    customer_name: str
    customer_phone: str
    total_price: float
    status: str
    order_detail: List[OrderDetailCreate]

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None
    status: Optional[str] = None
    order_detail: Optional[List[OrderDetailCreate]] = None

class OrderResponse(OrderBase):
    id: int
    order_detail: List[OrderDetailResponse]

    class Config:
        from_attributes = True
