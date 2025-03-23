from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./floristeria.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}) #Estandar
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db(): # Funcion  
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()