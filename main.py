from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import Base, engine
from login.routes import router as login_router
from products.routes import router as product_router
from users.routes import router as user_router
from orders.routes import router as order_routes
from order_detail.routes import router as order_detail_routes

# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine) 

# Iniciar la aplicación FastAPI
app = FastAPI()

app.add_middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"], 
                allow_headers=["*"]
                )


# Incluir las rutas de los endpoints
app.include_router(login_router, prefix="/api", tags=["Login"])
app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_routes)
app.include_router(order_detail_routes)


