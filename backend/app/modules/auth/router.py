from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.modules.auth.service import AuthService
from app.modules.auth.schemas import (
    UsuarioCreate, LoginRequest, TokenResponse,
    UsuarioResponse, CambiarRolRequest
)
from app.core.security import decode_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])

def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    from app.modules.auth.repository import UsuarioRepository
    usuario = UsuarioRepository(db).get_by_id(int(payload["sub"]))
    if not usuario or not usuario.activo:
        raise HTTPException(status_code=401, detail="Usuario no autorizado")
    return usuario

@router.post("/register", response_model=UsuarioResponse)
def registrar(data: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        service = AuthService(db)
        usuario = service.registrar_usuario(data.nombre, data.email, data.password, data.rol)
        return usuario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, request: Request, db: Session = Depends(get_db)):
    try:
        service = AuthService(db)
        ip = request.client.host if request.client else None
        token, usuario = service.login(data.email, data.password, ip)
        return TokenResponse(access_token=token, usuario=usuario)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/usuarios", response_model=list[UsuarioResponse])
def listar_usuarios(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.rol != "admin":
        raise HTTPException(status_code=403, detail="Acceso denegado")
    from app.modules.auth.repository import UsuarioRepository
    return UsuarioRepository(db).get_all()

@router.put("/usuarios/rol")
def cambiar_rol(
    data: CambiarRolRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.rol != "admin":
        raise HTTPException(status_code=403, detail="Solo administradores pueden cambiar roles")
    try:
        service = AuthService(db)
        usuario = service.cambiar_rol(current_user.id, data.usuario_id, data.nuevo_rol)
        return {"mensaje": "Rol actualizado", "usuario": usuario.email, "nuevo_rol": usuario.rol}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))