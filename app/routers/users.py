from fastapi import APIRouter, Query
from typing import Annotated, Any
from app.connections import get_db_query_result
from models.users import CheckCooperativeUserOut

router = APIRouter()


@router.get("/check_cooperative_member/", tags=["users"], response_model=CheckCooperativeUserOut)
async def member(dni: Annotated[str, Query(description="The DNI, NIF or NIE of a cooperative member.")]) -> Any:
    sql_query = f"SELECT COUNT(s.id) FROM `ert2_usuarios_v2` as u, `ert2_socios_v2` as s WHERE u.id=s.idusuario AND identificadorfiscal = '{
        dni}' AND s.estado=3;"
    result = get_db_query_result(sql_query)
    cooperative_user_exists = bool(int(result))
    return {
        "dni": dni,
        "cooperative_user_exists": cooperative_user_exists,
    }
