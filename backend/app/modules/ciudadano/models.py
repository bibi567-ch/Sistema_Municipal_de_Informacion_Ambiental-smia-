from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime,
    Text, Enum, Float, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database.connection import Base


class EstadoDenuncia(str, enum.Enum):
    PENDIENTE   = "pendiente"
    EN_REVISION = "en_revision"
    EN_PROCESO  = "en_proceso"
    RESUELTO    = "resuelto"
    CERRADO     = "cerrado"
    RECHAZADO   = "rechazado"


class CategoriaDenuncia(str, enum.Enum):
    RESIDUOS_SOLIDOS   = "residuos_solidos"
    CONTAMINACION_AGUA = "contaminacion_agua"
    CONTAMINACION_AIRE = "contaminacion_aire"
    RUIDO              = "ruido"
    TALA_ARBOLES       = "tala_arboles"
    OTRO               = "otro"


class Denuncia(Base):
    __tablename__ = "denuncias"

    id            = Column(Integer, primary_key=True, index=True)

    # Datos del ciudadano (puede ser anónimo)
    nombre_ciudadano  = Column(String(100), nullable=True)
    email_ciudadano   = Column(String(150), nullable=True)
    telefono          = Column(String(20),  nullable=True)
    es_anonima        = Column(Boolean, default=False)

    # Descripción del problema
    titulo      = Column(String(200), nullable=False)
    descripcion = Column(Text, nullable=False)
    categoria   = Column(Enum(CategoriaDenuncia), nullable=False)

    # Ubicación
    direccion   = Column(String(300), nullable=True)
    latitud     = Column(Float, nullable=True)
    longitud    = Column(Float, nullable=True)
    distrito    = Column(String(100), nullable=True)

    # Estado y seguimiento
    estado          = Column(Enum(EstadoDenuncia), default=EstadoDenuncia.PENDIENTE, nullable=False)
    codigo_seguimiento = Column(String(20), unique=True, index=True, nullable=False)
    tecnico_id      = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    resolucion      = Column(Text, nullable=True)

    # Fechas
    creado_en       = Column(DateTime, server_default=func.now())
    actualizado_en  = Column(DateTime, server_default=func.now(), onupdate=func.now())
    resuelto_en     = Column(DateTime, nullable=True)

    # Relaciones
    imagenes        = relationship("ImagenDenuncia", back_populates="denuncia", cascade="all, delete-orphan")
    historial       = relationship("HistorialEstado", back_populates="denuncia", cascade="all, delete-orphan")


class ImagenDenuncia(Base):
    __tablename__ = "imagenes_denuncia"

    id          = Column(Integer, primary_key=True, index=True)
    denuncia_id = Column(Integer, ForeignKey("denuncias.id"), nullable=False)
    url         = Column(String(500), nullable=False)
    nombre      = Column(String(200), nullable=True)
    creado_en   = Column(DateTime, server_default=func.now())

    denuncia    = relationship("Denuncia", back_populates="imagenes")


class HistorialEstado(Base):
    __tablename__ = "historial_estados_denuncia"

    id          = Column(Integer, primary_key=True, index=True)
    denuncia_id = Column(Integer, ForeignKey("denuncias.id"), nullable=False)
    estado_anterior = Column(Enum(EstadoDenuncia), nullable=True)
    estado_nuevo    = Column(Enum(EstadoDenuncia), nullable=False)
    comentario      = Column(Text, nullable=True)
    usuario_id      = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    fecha_cambio    = Column(DateTime, server_default=func.now())

    denuncia    = relationship("Denuncia", back_populates="historial")