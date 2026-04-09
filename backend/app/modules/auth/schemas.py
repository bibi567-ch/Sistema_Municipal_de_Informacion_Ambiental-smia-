from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.modules.auth.models import RolUsuario

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str
    rol: RolUsuario = RolUsuario.TECNICO

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    rol: RolUsuario
    activo: bool
    creado_en: datetime

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse

class CambiarRolRequest(BaseModel):
    usuario_id: int
    nuevo_rol: RolUsuario