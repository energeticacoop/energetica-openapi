from pydantic import BaseModel


class CheckCooperativeUserOut(BaseModel):
    dni: str
    cooperative_user_exists: bool
