from pydantic import BaseModel, Field


class RiteReplacementValues(BaseModel):
    data: dict[str, str] = Field(
        example={
            "{direccion}": "Avenida Ramón Pradera, 12",
            "{CP}": "47009",
            "{municipio}": "Valladolid"
        }
    )


class MgeReplacementValues(BaseModel):
    data: dict[str, str] = Field(
        example={
            "<Dirección>": "Avenida Ramón Pradera, 12",
            "<Nombre>": "Juan"
        }
    )
