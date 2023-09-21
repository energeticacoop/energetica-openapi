from pydantic import BaseModel


class CheckCooperativeUserOut(BaseModel):
    dni: str
    cooperative_user_exists: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "dni": "00000000T",
                    "cooperative_user_exists": True,
                }
            ]
        }
    }
