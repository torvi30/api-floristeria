# Definición del modelo de Usuario
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)


# Esquema de Pydantic para validación de datos
class UserCreate(BaseModel):
    username: str
    password: str