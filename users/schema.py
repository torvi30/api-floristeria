from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    password: str

# Esquema para crear un usuario
class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

# Esquema para solicitud de recuperación de contraseña
class PasswordResetRequest(BaseModel):
    email: EmailStr

# Esquema para restablecer la contraseña
class PasswordReset(BaseModel):
    token: str
    new_password: str