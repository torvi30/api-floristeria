from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from db import Base, engine
from login.routes import router as login_router
from products.routes import router as product_router
from users.routes import router as user_router
from orders.routes import router as order_router

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
app.include_router(user_router, prefix="/api", tags=["Users"])
app.include_router(product_router, prefix="/api", tags=["Products"])
app.include_router(order_router, prefix="/api", tags=["Orders"])

@app.get("/")
async def redirect_to_docs(request: Request):
    return RedirectResponse(url="/docs")