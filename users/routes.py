from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import  get_db
from users.model import User
from users.schema import UserCreate
from encrypt import hash_password



router = APIRouter(prefix="", tags=["Register"])
# Endpoint para registrar usuarios
@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.username == user.username).first() # Consulta a la BD
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Crear nuevo usuario
    new_user = User(username=user.username, password_hash=hash_password(user.password)) # Encripta contraseña
    db.add(new_user)
    db.commit() # Subir los cambios
    db.refresh(new_user) # Recargar la 
    
    return {"message": "Usuario registrado exitosamente"}
