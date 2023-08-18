from fastapi import APIRouter, Query
from typing import Annotated, Any
from dependencies import get_db_connection
from models.users import CheckCooperativeUserOut

router = APIRouter()


def check_cooperative_member(dni: str) -> bool:
    connection = get_db_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        sql_query = f"SELECT COUNT(s.id) FROM `ert2_usuarios_v2` as u, `ert2_socios_v2` as s WHERE u.id=s.idusuario AND identificadorfiscal = '{dni}' AND s.estado=3;"
        cursor.execute(sql_query)
        count_result = cursor.fetchone()[0]
    except mysql.connector.Error as e:
        print("Error:", e)
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return bool(int(count_result))


@router.get("/check_cooperative_member/", tags=["users"], response_model=CheckCooperativeUserOut)
async def member(dni: Annotated[str, Query(description="The DNI, NIF or NIE of a cooperative member.", pattern=r'^\d{8}[a-zA-Z]$')]) -> Any:
    cooperative_user_exists = check_cooperative_member(dni)
    return {
        "dni": dni,
        "cooperative_user_exists": cooperative_user_exists,
    }
