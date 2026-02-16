import uuid
from sqlalchemy import UUID, Column, DateTime, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    perfil = relationship("Perfil", back_populates="usuario", uselist=False) # Relacion 1 a 1

class Perfil(Base):
    __tablename__ = "perfil"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    nombre = Column(String)
    pais = Column(String)
    usuario_id = Column(
        String(36),
        ForeignKey("usuario.id", unique=True)
    )
    usuario = relationship("Usuario", back_populates="perfil", uselist=False)

class Acceso(Base):
    __tablename__ = "acceso"
    id = Column(
        String,
        primary_key=True,
        index=True
    )
    ultimo_login = Column(
        DateTime
    )

class CategoriaModel(Base):
    __tablename__ = "categoria"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
        index=True
    )
    nombre = Column(String)
