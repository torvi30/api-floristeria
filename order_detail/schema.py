from pydantic import BaseModel

class OrderDetailBase(BaseModel):
    order_id: int
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
