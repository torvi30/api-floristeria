from fastapi import FastAPI
from db import Base, engine
from login.routes import router as login_router

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine) 

# Iniciar la aplicación FastAPI
app = FastAPI()

app.include_router(login_router, prefix="/api", tags=["login"])

