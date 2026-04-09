from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime
from typing import Optional
from app.modules.auth.models import Usuario, BitacoraAccion, RolUsuario

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email).first()

    def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.id == usuario_id).first()

    def get_all(self):
        return self.db.query(Usuario).all()

    def create(self, nombre: str, email: str, hashed_password: str, rol: RolUsuario) -> Usuario:
        usuario = Usuario(
            nombre=nombre,
            email=email,
            hashed_password=hashed_password,
            rol=rol,
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update_intentos_fallidos(self, usuario: Usuario, intentos: int, bloqueado_hasta=None):
        usuario.intentos_fallidos = intentos
        usuario.bloqueado_hasta = bloqueado_hasta
        self.db.commit()

    def update_rol(self, usuario: Usuario, nuevo_rol: RolUsuario) -> Usuario:
        usuario.rol = nuevo_rol
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def update_estado(self, usuario: Usuario, activo: bool) -> Usuario:
        usuario.activo = activo
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

class BitacoraRepository:
    def __init__(self, db: Session):
        self.db = db

    def registrar(self, accion: str, modulo: str, usuario_id=None,
                  usuario_email=None, ip_origen=None, detalle=None):
        log = BitacoraAccion(
            usuario_id=usuario_id,
            usuario_email=usuario_email,
            accion=accion,
            modulo=modulo,
            ip_origen=ip_origen,
            detalle=detalle,
        )
        self.db.add(log)
        self.db.commit()

    def get_logs(self, desde: datetime = None, hasta: datetime = None):
        query = self.db.query(BitacoraAccion)
        if desde:
            query = query.filter(BitacoraAccion.fecha_hora >= desde)
        if hasta:
            query = query.filter(BitacoraAccion.fecha_hora <= hasta)
        return query.order_by(BitacoraAccion.fecha_hora.desc()).all()