import random
import string
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from app.modules.ciudadano.repository import DenunciaRepository, HistorialRepository
from app.modules.ciudadano.models import EstadoDenuncia, CategoriaDenuncia
from app.modules.ciudadano.schemas import DenunciaCreate, CambiarEstadoRequest


def _generar_codigo() -> str:
    """Genera un código único de seguimiento tipo DEN-2026-XXXX."""
    anio = datetime.utcnow().year
    sufijo = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"DEN-{anio}-{sufijo}"


class CiudadanoService:
    def __init__(self, db: Session):
        self.repo      = DenunciaRepository(db)
        self.historial = HistorialRepository(db)

    # ──────────────────────────────────────────
    # Crear denuncia (ciudadano o técnico)
    # ──────────────────────────────────────────
    def crear_denuncia(self, datos: DenunciaCreate):
        # Generar código único (reintenta si colisiona)
        for _ in range(5):
            codigo = _generar_codigo()
            if not self.repo.get_by_codigo(codigo):
                break

        # Si es anónima, omitir datos personales
        payload = datos.model_dump()
        if datos.es_anonima:
            payload["nombre_ciudadano"] = None
            payload["email_ciudadano"]  = None
            payload["telefono"]         = None

        payload["codigo_seguimiento"] = codigo
        payload["estado"]             = EstadoDenuncia.PENDIENTE

        denuncia = self.repo.create(payload)

        # Registrar primer estado en historial
        self.historial.registrar_cambio(
            denuncia_id=denuncia.id,
            estado_anterior=None,
            estado_nuevo=EstadoDenuncia.PENDIENTE,
            comentario="Denuncia registrada en el sistema.",
        )
        return denuncia

    # ──────────────────────────────────────────
    # Consulta pública por código
    # ──────────────────────────────────────────
    def consultar_seguimiento(self, codigo: str):
        denuncia = self.repo.get_by_codigo(codigo.upper())
        if not denuncia:
            raise ValueError(f"No se encontró denuncia con código: {codigo}")
        return denuncia

    # ──────────────────────────────────────────
    # Listar para técnicos / admin
    # ──────────────────────────────────────────
    def listar_denuncias(
        self,
        estado: Optional[EstadoDenuncia] = None,
        categoria: Optional[CategoriaDenuncia] = None,
        tecnico_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 50,
    ):
        return self.repo.get_all(
            estado=estado,
            categoria=categoria,
            tecnico_id=tecnico_id,
            skip=skip,
            limit=limit,
        )

    def obtener_denuncia(self, denuncia_id: int):
        denuncia = self.repo.get_by_id(denuncia_id)
        if not denuncia:
            raise ValueError("Denuncia no encontrada")
        return denuncia

    # ──────────────────────────────────────────
    # Cambiar estado (técnico / admin)
    # ──────────────────────────────────────────
    def cambiar_estado(
        self,
        denuncia_id: int,
        datos: CambiarEstadoRequest,
        usuario_id: int,
    ):
        denuncia = self.repo.get_by_id(denuncia_id)
        if not denuncia:
            raise ValueError("Denuncia no encontrada")

        # Validar transición de estado
        transiciones_validas = {
            EstadoDenuncia.PENDIENTE:   [EstadoDenuncia.EN_REVISION, EstadoDenuncia.RECHAZADO],
            EstadoDenuncia.EN_REVISION: [EstadoDenuncia.EN_PROCESO,  EstadoDenuncia.RECHAZADO],
            EstadoDenuncia.EN_PROCESO:  [EstadoDenuncia.RESUELTO,    EstadoDenuncia.EN_REVISION],
            EstadoDenuncia.RESUELTO:    [EstadoDenuncia.CERRADO],
            EstadoDenuncia.CERRADO:     [],
            EstadoDenuncia.RECHAZADO:   [],
        }
        if datos.nuevo_estado not in transiciones_validas.get(denuncia.estado, []):
            raise ValueError(
                f"No se puede pasar de '{denuncia.estado}' a '{datos.nuevo_estado}'"
            )

        estado_anterior = denuncia.estado
        denuncia = self.repo.update_estado(
            denuncia,
            datos.nuevo_estado,
            resolucion=datos.resolucion,
        )
        self.historial.registrar_cambio(
            denuncia_id=denuncia.id,
            estado_anterior=estado_anterior,
            estado_nuevo=datos.nuevo_estado,
            usuario_id=usuario_id,
            comentario=datos.comentario,
        )
        return denuncia

    # ──────────────────────────────────────────
    # Asignar técnico
    # ──────────────────────────────────────────
    def asignar_tecnico(self, denuncia_id: int, tecnico_id: int, admin_id: int):
        denuncia = self.repo.get_by_id(denuncia_id)
        if not denuncia:
            raise ValueError("Denuncia no encontrada")

        denuncia = self.repo.asignar_tecnico(denuncia, tecnico_id)
        self.historial.registrar_cambio(
            denuncia_id=denuncia.id,
            estado_anterior=denuncia.estado,
            estado_nuevo=denuncia.estado,
            usuario_id=admin_id,
            comentario=f"Técnico ID {tecnico_id} asignado a la denuncia.",
        )
        return denuncia