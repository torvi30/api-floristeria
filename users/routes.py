from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from users.model import User
from users.schema import UserCreate, PasswordResetRequest, PasswordReset
from encrypt import hash_password
from users.email_utils import send_reset_email  # Función para enviar correos electrónicos
import secrets

router = APIRouter()

# Endpoint para registrar usuarios
@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Crear nuevo usuario
    new_user = User(username=user.username, email=user.email, password_hash=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Usuario registrado exitosamente"}

# Endpoint para recuperación de contraseña
@router.post("/password-recovery/")
def password_recovery(request: PasswordResetRequest, db: Session = Depends(get_db)):
    # Buscar usuario por email
    user = db.query(User).filter(User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Generar un token único para el enlace de recuperación
    reset_token = secrets.token_urlsafe(32)

    # Guardar el token en la base de datos
    user.reset_token = reset_token
    db.commit()
    db.refresh(user)

    # Enviar correo electrónico con el enlace de recuperación
    reset_link = f"http://127.0.0.1:5500/floristeria/login/reset-password.html?token={reset_token}"
    send_reset_email(user.email, reset_link)

    return {"message": "Correo de recuperación enviado"}

# Endpoint para restablecer la contraseña
@router.post("/reset-password/")
def reset_password(data: PasswordReset, db: Session = Depends(get_db)):
    # Buscar usuario por token
    user = db.query(User).filter(User.reset_token == data.token).first()
    if not user:
        raise HTTPException(status_code=400, detail="Token invalido o expirado")

    # Actualizar la contraseña
    user.password_hash = hash_password(data.new_password)
    user.reset_token = None  # Eliminar el token después de usarlo
    db.commit()
    db.refresh(user)

    return {"message": "Contraseña actualizada exitosamente"}
