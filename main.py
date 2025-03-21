from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import bcrypt

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./floristeria.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definición del modelo de Usuario
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)

# Esquema de Pydantic para validación de datos
class UserCreate(BaseModel):
    username: str
    password: str

# Iniciar la aplicación FastAPI
app = FastAPI()

def get_db(): # Funcion  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para hash de contraseñas
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') # Estandar de la libreria

# Función para desencriptar contraseñas
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))  # Estandar de la libreria

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
