from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class RegistroReproceso(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime = Field(default_factory=datetime.utcnow)
    codigo_producto: str
    categoria: str
    lote: Optional[str] = None
    observaciones: Optional[str] = None