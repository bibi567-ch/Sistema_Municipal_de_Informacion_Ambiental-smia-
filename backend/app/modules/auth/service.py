from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from app.modules.auth.repository import UsuarioRepository, BitacoraRepository
from app.modules.auth.models import RolUsuario
from app.core.security import hash_password, verify_password, create_access_token

MAX_INTENTOS = 3
BLOQUEO_MINUTOS = 15

class AuthService:
    def __init__(self, db: Session):
        self.repo = UsuarioRepository(db)
        self.bitacora = BitacoraRepository(db)

    def registrar_usuario(self, nombre: str, email: str, password: str, rol: RolUsuario):
        existente = self.repo.get_by_email(email)
        if existente:
            raise ValueError("El email ya está registrado")
        hashed = hash_password(password)
        usuario = self.repo.create(nombre, email, hashed, rol)
        self.bitacora.registrar(
            accion="REGISTRO_USUARIO",
            modulo="auth",
            usuario_email=email,
            detalle=f"Usuario {nombre} registrado con rol {rol}"
        )
        return usuario

    def login(self, email: str, password: str, ip_origen: str = None):
        usuario = self.repo.get_by_email(email)

        if not usuario:
            raise ValueError("Credenciales incorrectas")

        # Verificar si está bloqueado (HU-01.1)
        if usuario.bloqueado_hasta and datetime.utcnow() < usuario.bloqueado_hasta:
            minutos = int((usuario.bloqueado_hasta - datetime.utcnow()).seconds / 60)
            raise ValueError(f"Cuenta bloqueada. Intente en {minutos} minutos")

        if not usuario.activo:
            raise ValueError("Cuenta inactiva. Contacte al administrador.")

        # Verificar contraseña
        if not verify_password(password, usuario.hashed_password):
            intentos = usuario.intentos_fallidos + 1
            bloqueado_hasta = None
            if intentos >= MAX_INTENTOS:
                bloqueado_hasta = datetime.utcnow() + timedelta(minutes=BLOQUEO_MINUTOS)
                intentos = 0
            self.repo.update_intentos_fallidos(usuario, intentos, bloqueado_hasta)
            restantes = MAX_INTENTOS - intentos
            raise ValueError(f"Contraseña incorrecta. Intentos restantes: {restantes}")

        # Login exitoso — resetear intentos
        self.repo.update_intentos_fallidos(usuario, 0, None)
        token = create_access_token({"sub": str(usuario.id), "rol": usuario.rol})
        self.bitacora.registrar(
            accion="LOGIN_EXITOSO",
            modulo="auth",
            usuario_id=usuario.id,
            usuario_email=email,
            ip_origen=ip_origen,
        )
        return token, usuario

    def cambiar_rol(self, admin_id: int, usuario_id: int, nuevo_rol: RolUsuario):
        usuario = self.repo.get_by_id(usuario_id)
        if not usuario:
            raise ValueError("Usuario no encontrado")
        usuario_actualizado = self.repo.update_rol(usuario, nuevo_rol)
        self.bitacora.registrar(
            accion="CAMBIO_ROL",
            modulo="auth",
            usuario_id=admin_id,
            detalle=f"Rol de usuario {usuario_id} cambiado a {nuevo_rol}"
        )
        return usuario_actualizado