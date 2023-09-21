from pydantic import BaseModel, Field


class ReplacementValues(BaseModel):
    data: dict[str, str] = Field(
        example={
            "{direccion}": "Avenida Ramón Pradera, 12",
            "{CP}": "47009",
            "{municipio}": "Valladolid"
        }
    )
