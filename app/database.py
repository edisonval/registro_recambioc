from sqlmodel import SQLModel, create_engine

DATABASE_URL = "sqlite:///./reproceso.db"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True muestra las consultas en consola

def crear_db():
    SQLModel.metadata.create_all(engine)