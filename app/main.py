from fastapi import FastAPI
from app.database import crear_db

app = FastAPI()

# Crear la base de datos al iniciar el servidor
@app.on_event("startup")
def startup():
    crear_db()

@app.get("/")
def read_root():
    return{"mensaje": "aplicacion de registro de proceso funcionando"}