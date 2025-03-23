from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import Base, engine, get_db
from users.model import User, UserCreate
from encrypt import hash_password, verify_password

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine) 

# Iniciar la aplicación FastAPI
app = FastAPI()

# Endpoint para registrar usuarios
@app.post("/register/")
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

# Endpoint para login
@app.post("/login/")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Buscar usuario en la base de datos
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Autenticación fallida")
    
    return {"message": "Autenticación satisfactoria"}
