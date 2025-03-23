from pydantic import BaseModel

# Esquema de Pydantic para validación de datos
class UserCreate(BaseModel):
    username: str
    password: str