from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, nullable=False, default="pendiente")

    details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")
