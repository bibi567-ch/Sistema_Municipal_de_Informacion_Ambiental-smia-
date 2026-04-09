from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
import enum
from app.database.connection import Base

class RolUsuario(str, enum.Enum):
    ADMIN = "admin"
    TECNICO = "tecnico"
    ADMINISTRATIVO = "administrativo"
    CIUDADANO = "ciudadano"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuario), default=RolUsuario.TECNICO, nullable=False)
    activo = Column(Boolean, default=True)
    intentos_fallidos = Column(Integer, default=0)
    bloqueado_hasta = Column(DateTime, nullable=True)
    creado_en = Column(DateTime, server_default=func.now())
    actualizado_en = Column(DateTime, server_default=func.now(), onupdate=func.now())

class BitacoraAccion(Base):
    __tablename__ = "bitacora_acciones"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, nullable=True)
    usuario_email = Column(String(150), nullable=True)
    accion = Column(String(200), nullable=False)
    modulo = Column(String(100), nullable=False)
    ip_origen = Column(String(45), nullable=True)
    fecha_hora = Column(DateTime, server_default=func.now())
    detalle = Column(String(500), nullable=True)