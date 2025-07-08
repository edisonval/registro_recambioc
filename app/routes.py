from fastapi import APIRouter
from sqlmodel import Session
from app.models import RegistroReproceso
from app.database import engine

router = APIRouter()

@router.post("/registrar")
def registrar_reproceso(registro: RegistroReproceso):
    with Session(engine) as session:
        session.add(registro)
        session.commit()
        session.refresh(registro)
    return {"mensaje": "Registro guardado correctamente", "id": registro.id}


@router.get("/consultar")
def consultar_reprocesos():
    with Session(engine) as session:
        registros = session.query(RegistroReproceso).all()
        return registros

