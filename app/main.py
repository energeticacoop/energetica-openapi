from typing import Annotated, Any
from fastapi import FastAPI, Query
from pydantic import BaseModel

import mysql.connector
from dotenv import dotenv_values
import os

script_dir = os.path.dirname(__file__)  # Get the directory of your script
dotenv_path = os.path.join(script_dir, ".env")
db_config = dotenv_values(dotenv_path)


description = """
Energética Coop's API for cooperative users, clients and services ⚡
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users, both cooperative members and clients",
    },

]


app = FastAPI(
    openapi_url="/api/v1/openapi.json",  # Specify the OpenAPI URL
    title="Energética Coop API",  # Set your custom title here
    version="0.0.1",
    description=description,
)


class CheckCooperativeUserOut(BaseModel):
    dni: str
    cooperative_user_exists: bool


def check_cooperative_member(dni: str) -> bool:

    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            # Define the SQL query
            sql_query = f"SELECT COUNT(s.id) FROM `ert2_usuarios_v2` as u, `ert2_socios_v2` as s WHERE u.id=s.idusuario AND identificadorfiscal = '{dni}' AND s.estado=3;"
            # Create a cursor object to execute the query
            cursor = connection.cursor()
            # Execute the query
            cursor.execute(sql_query)

            # Fetch the result
            count_result = cursor.fetchone()[0]

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

    return bool(int(count_result))


@app.get("/check_cooperative_member/", tags=["users"], response_model=CheckCooperativeUserOut)
async def member(dni: Annotated[str, Query(description="The DNI, NIF or NIE of a cooperative member.", pattern=r'^\d{8}[a-zA-Z]$')]) -> Any:
    cooperative_user_exists = check_cooperative_member(dni)
    return {
        "dni": dni,
        "cooperative_user_exists": cooperative_user_exists,
    }
