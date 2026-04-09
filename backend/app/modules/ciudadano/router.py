from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional, List

from app.database.connection import get_db
from app.modules.ciudadano.service import CiudadanoService
from app.modules.ciudadano.schemas import (
    DenunciaCreate,
    DenunciaResponse,
    DenunciaResumenResponse,
    SeguimientoPublicoResponse,
    CambiarEstadoRequest,
    AsignarTecnicoRequest,
)
from app.modules.ciudadano.models import EstadoDenuncia, CategoriaDenuncia
from app.core.security import decode_token
from app.modules.auth.repository import UsuarioRepository
from fastapi import Request

router = APIRouter(prefix="/ciudadano", tags=["Ciudadano — Denuncias"])


# ─────────────────────────────────────────────
# Helpers de autenticación
# ─────────────────────────────────────────────

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    usuario = UsuarioRepository(db).get_by_id(int(payload["sub"]))
    if not usuario or not usuario.activo:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    return usuario


def require_tecnico_o_admin(current_user=Depends(get_current_user)):
    if current_user.rol not in ("tecnico", "admin", "administrativo"):
        raise HTTPException(status_code=403, detail="Acceso denegado")
    return current_user


def require_admin(current_user=Depends(get_current_user)):
    if current_user.rol != "admin":
        raise HTTPException(status_code=403, detail="Solo administradores")
    return current_user


# ─────────────────────────────────────────────
# Endpoints PÚBLICOS (sin autenticación)
# ─────────────────────────────────────────────

@router.post(
    "/denuncias",
    response_model=DenunciaResumenResponse,
    status_code=201,
    summary="Crear denuncia ambiental",
)
def crear_denuncia(datos: DenunciaCreate, db: Session = Depends(get_db)):
    """
    Cualquier ciudadano puede registrar una denuncia.
    Retorna el código de seguimiento para consultas futuras.
    """
    try:
        service = CiudadanoService(db)
        return service.crear_denuncia(datos)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.get(
    "/seguimiento/{codigo}",
    response_model=SeguimientoPublicoResponse,
    summary="Consultar estado de denuncia por código",
)
def consultar_seguimiento(codigo: str, db: Session = Depends(get_db)):
    """
    Endpoint público: el ciudadano ingresa su código DEN-XXXX-YYYYYY
    y ve el estado actual e historial de cambios.
    """
    try:
        service = CiudadanoService(db)
        return service.consultar_seguimiento(codigo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


# ─────────────────────────────────────────────
# Endpoints PROTEGIDOS (técnicos y admins)
# ─────────────────────────────────────────────

@router.get(
    "/denuncias",
    response_model=List[DenunciaResumenResponse],
    summary="Listar denuncias (técnico/admin)",
)
def listar_denuncias(
    estado:     Optional[EstadoDenuncia]    = Query(None),
    categoria:  Optional[CategoriaDenuncia] = Query(None),
    tecnico_id: Optional[int]               = Query(None),
    skip:  int = Query(0,  ge=0),
    limit: int = Query(50, ge=1, le=200),
    _=Depends(require_tecnico_o_admin),
    db: Session = Depends(get_db),
):
    service = CiudadanoService(db)
    return service.listar_denuncias(
        estado=estado,
        categoria=categoria,
        tecnico_id=tecnico_id,
        skip=skip,
        limit=limit,
    )


@router.get(
    "/denuncias/{denuncia_id}",
    response_model=DenunciaResponse,
    summary="Detalle completo de una denuncia",
)
def obtener_denuncia(
    denuncia_id: int,
    _=Depends(require_tecnico_o_admin),
    db: Session = Depends(get_db),
):
    try:
        service = CiudadanoService(db)
        return service.obtener_denuncia(denuncia_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.patch(
    "/denuncias/{denuncia_id}/estado",
    response_model=DenunciaResumenResponse,
    summary="Cambiar estado de una denuncia",
)
def cambiar_estado(
    denuncia_id: int,
    datos: CambiarEstadoRequest,
    current_user=Depends(require_tecnico_o_admin),
    db: Session = Depends(get_db),
):
    try:
        service = CiudadanoService(db)
        return service.cambiar_estado(denuncia_id, datos, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.patch(
    "/denuncias/{denuncia_id}/asignar",
    response_model=DenunciaResumenResponse,
    summary="Asignar técnico a una denuncia (solo admin)",
)
def asignar_tecnico(
    denuncia_id: int,
    datos: AsignarTecnicoRequest,
    current_user=Depends(require_admin),
    db: Session = Depends(get_db),
):
    try:
        service = CiudadanoService(db)
        return service.asignar_tecnico(denuncia_id, datos.tecnico_id, current_user.id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e