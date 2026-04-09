from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, List
from datetime import datetime
from app.modules.ciudadano.models import (
    Denuncia, ImagenDenuncia, HistorialEstado,
    EstadoDenuncia, CategoriaDenuncia
)


class DenunciaRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, denuncia_id: int) -> Optional[Denuncia]:
        return self.db.query(Denuncia).filter(Denuncia.id == denuncia_id).first()

    def get_by_codigo(self, codigo: str) -> Optional[Denuncia]:
        return self.db.query(Denuncia).filter(
            Denuncia.codigo_seguimiento == codigo
        ).first()

    def get_all(
        self,
        estado: Optional[EstadoDenuncia] = None,
        categoria: Optional[CategoriaDenuncia] = None,
        tecnico_id: Optional[int] = None,
        skip: int = 0,
        limit: int = 50,
    ) -> List[Denuncia]:
        query = self.db.query(Denuncia)
        if estado:
            query = query.filter(Denuncia.estado == estado)
        if categoria:
            query = query.filter(Denuncia.categoria == categoria)
        if tecnico_id:
            query = query.filter(Denuncia.tecnico_id == tecnico_id)
        return (
            query.order_by(Denuncia.creado_en.desc())
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, data: dict) -> Denuncia:
        denuncia = Denuncia(**data)
        self.db.add(denuncia)
        self.db.commit()
        self.db.refresh(denuncia)
        return denuncia

    def update_estado(
        self,
        denuncia: Denuncia,
        nuevo_estado: EstadoDenuncia,
        resolucion: Optional[str] = None,
    ) -> Denuncia:
        denuncia.estado = nuevo_estado
        if resolucion:
            denuncia.resolucion = resolucion
        if nuevo_estado in (EstadoDenuncia.RESUELTO, EstadoDenuncia.CERRADO):
            denuncia.resuelto_en = datetime.utcnow()
        self.db.commit()
        self.db.refresh(denuncia)
        return denuncia

    def asignar_tecnico(self, denuncia: Denuncia, tecnico_id: int) -> Denuncia:
        denuncia.tecnico_id = tecnico_id
        self.db.commit()
        self.db.refresh(denuncia)
        return denuncia

    def count_by_estado(self) -> dict:
        """Retorna conteo agrupado por estado (para dashboard)."""
        rows = (
            self.db.query(Denuncia.estado, func.count())
            .group_by(Denuncia.estado)
            .all()
        )
        return {estado: total for estado, total in rows}


class HistorialRepository:
    def __init__(self, db: Session):
        self.db = db

    def registrar_cambio(
        self,
        denuncia_id: int,
        estado_anterior: Optional[EstadoDenuncia],
        estado_nuevo: EstadoDenuncia,
        usuario_id: Optional[int] = None,
        comentario: Optional[str] = None,
    ) -> HistorialEstado:
        entrada = HistorialEstado(
            denuncia_id=denuncia_id,
            estado_anterior=estado_anterior,
            estado_nuevo=estado_nuevo,
            usuario_id=usuario_id,
            comentario=comentario,
        )
        self.db.add(entrada)
        self.db.commit()
        return entrada

    def get_historial(self, denuncia_id: int) -> List[HistorialEstado]:
        return (
            self.db.query(HistorialEstado)
            .filter(HistorialEstado.denuncia_id == denuncia_id)
            .order_by(HistorialEstado.fecha_cambio.asc())
            .all()
        )