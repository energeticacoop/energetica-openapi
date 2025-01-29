from pydantic import BaseModel


class NumericDataResponse(BaseModel):
    value: int
    unit: str
    timestamp: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "value": 1312,
                    "unit": "unidades",
                    "timestamp": "2023-10-20T12:34:56.789012"
                }
            ]
        }
    }
