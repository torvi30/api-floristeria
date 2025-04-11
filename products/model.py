from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
