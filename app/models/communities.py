from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Community(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    name: str
    address: str
    activa: bool
    abierta: bool
    revisable: bool
    potencia_instalada: str
    superficie: str
    tipo: str
    enlace: str
    caracteristicas: str
    participantes_maximos: int
    participantes_actuales: int
    emisiones_evitadas: str
    produccion_anual_estimada: str
    produccion_anual_real: str
    autoconsumo: str
    propietario: str
    deleted_at: Optional[datetime]
    estado: str
    localizacion: str
    localidad: str
    provincia: str
    promotor: str
    gobernanza: str
    contacto: Optional[str]
    fecha_funcionamiento: datetime
    calculo_potencia_instalacion: str
    calculo_potencia_pico: str
    calculo_horas_equivalentes_kwp: str
    calculo_precio_kwh: str
    calculo_cuota_anual_antes_impuestos: str
    foto_cel: str

    model_config = {
        "json_schema_extra": {
            "examples": [
            ]
        }
    }
