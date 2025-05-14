from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import  get_db
from users.model import User
from users.schema import UserBase
from encrypt import verify_password


router = APIRouter()

# Endpoint para login
@router.post("/login/")
def login(user: UserBase, db: Session = Depends(get_db)):
    # Buscar usuario en la base de datos
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Autenticación fallida")
    
    return {"message": "Autenticación satisfactoria"}
