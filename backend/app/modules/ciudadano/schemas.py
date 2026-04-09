from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional, List
from datetime import datetime
from app.modules.ciudadano.models import EstadoDenuncia, CategoriaDenuncia


# ──────────────────────────────────────────
# Schemas de entrada (requests)
# ──────────────────────────────────────────

class DenunciaCreate(BaseModel):
    titulo: str
    descripcion: str
    categoria: CategoriaDenuncia

    # Ciudadano (opcional si es anónima)
    nombre_ciudadano: Optional[str] = None
    email_ciudadano:  Optional[EmailStr] = None
    telefono:         Optional[str] = None
    es_anonima:       bool = False

    # Ubicación
    direccion: Optional[str] = None
    latitud:   Optional[float] = None
    longitud:  Optional[float] = None
    distrito:  Optional[str] = None

    @field_validator("titulo")
    @classmethod
    def titulo_no_vacio(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("El título no puede estar vacío")
        return v.strip()

    @field_validator("descripcion")
    @classmethod
    def descripcion_minima(cls, v: str) -> str:
        if len(v.strip()) < 20:
            raise ValueError("La descripción debe tener al menos 20 caracteres")
        return v.strip()


class CambiarEstadoRequest(BaseModel):
    nuevo_estado: EstadoDenuncia
    comentario:   Optional[str] = None
    resolucion:   Optional[str] = None


class AsignarTecnicoRequest(BaseModel):
    tecnico_id: int


# ──────────────────────────────────────────
# Schemas de salida (responses)
# ──────────────────────────────────────────

class ImagenDenunciaResponse(BaseModel):
    id:        int
    url:       str
    nombre:    Optional[str]
    creado_en: datetime

    class Config:
        from_attributes = True


class HistorialEstadoResponse(BaseModel):
    id:              int
    estado_anterior: Optional[EstadoDenuncia]
    estado_nuevo:    EstadoDenuncia
    comentario:      Optional[str]
    fecha_cambio:    datetime

    class Config:
        from_attributes = True


class DenunciaResponse(BaseModel):
    id:                 int
    codigo_seguimiento: str
    titulo:             str
    descripcion:        str
    categoria:          CategoriaDenuncia
    estado:             EstadoDenuncia

    # Ciudadano (oculto si es anónima)
    nombre_ciudadano:  Optional[str]
    email_ciudadano:   Optional[str]
    es_anonima:        bool

    # Ubicación
    direccion: Optional[str]
    latitud:   Optional[float]
    longitud:  Optional[float]
    distrito:  Optional[str]

    # Resolución
    tecnico_id: Optional[int]
    resolucion: Optional[str]

    # Fechas
    creado_en:      datetime
    actualizado_en: datetime
    resuelto_en:    Optional[datetime]

    imagenes: List[ImagenDenunciaResponse] = []
    historial: List[HistorialEstadoResponse] = []

    class Config:
        from_attributes = True


class DenunciaResumenResponse(BaseModel):
    """Vista reducida para listados (sin historial completo)."""
    id:                 int
    codigo_seguimiento: str
    titulo:             str
    categoria:          CategoriaDenuncia
    estado:             EstadoDenuncia
    distrito:           Optional[str]
    creado_en:          datetime

    class Config:
        from_attributes = True


class SeguimientoPublicoResponse(BaseModel):
    """Lo que ve un ciudadano al consultar su código de seguimiento."""
    codigo_seguimiento: str
    titulo:             str
    categoria:          CategoriaDenuncia
    estado:             EstadoDenuncia
    creado_en:          datetime
    resuelto_en:        Optional[datetime]
    historial:          List[HistorialEstadoResponse] = []

    class Config:
        from_attributes = True