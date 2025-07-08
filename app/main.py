from fastapi import FastAPI
from app.database import crear_db
from app.routes import router
from fastapi.staticfiles import StaticFiles
import os


app = FastAPI()
app.include_router(router)
# Servir archivos estáticos
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# Crear la base de datos al iniciar el servidor
@app.on_event("startup")
def startup():
    crear_db()

@app.get("/")
def read_root():
    return{"mensaje": "aplicacion de registro de proceso funcionando"}

