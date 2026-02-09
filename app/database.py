from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

CADENA_CONEXION = "postgres://videojuegos:videojuegos@localhost:5432/bd_videojuegos"

engine = create_engine(CADENA_CONEXION)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
