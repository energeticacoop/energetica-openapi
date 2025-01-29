import requests
from fastapi import APIRouter, HTTPException
from pydantic import TypeAdapter, create_model

from app.connections import get_db_query_result
from app.models.communities import Community

router = APIRouter()

# Create a dynamic Pydantic model for Community using pydantic.create_model
CommunityModel = create_model(
    "CommunityModel",
    **{name: (type_, ...) for name, type_ in Community.__annotations__.items()}
)


@router.get("/communities/{community_id}", tags=["communities"], response_model=Community)
async def get_community(community_id: int) -> Community:
    # Connect to MySQL database

    sql_query = f"SELECT * FROM cels WHERE id = {community_id};"
    cel_data = get_db_query_result(sql_query, database="cels")

    if not cel_data:
        raise HTTPException(status_code=404, detail="Community not found")

    cel = Community(**cel_data)
    ta = TypeAdapter(Community)
    return ta.validate_python(cel)


class CelNotFoundException(Exception):
    def __init__(self, message="Energy Community not found"):
        self.message = message
        super().__init__(self.message)


@router.get("/communities/coverage/{community_id}", tags=["communities"])
async def get_community_coverage(community_id: int) -> float:

    clients_api_url = f"""https://gestion.comunidadessolares.org/api/clients?cel={
        community_id}"""
    cel_api_url = f"""https://gestion.comunidadessolares.org/api/cels/{
        community_id}"""
    try:

        # Send a GET request to the API
        response = requests.get(cel_api_url)
        response.raise_for_status()  # This will raise an exception for non-200 status codes

        # Parse the JSON response
        data = response.json()

        if len(data["data"]) == 0:
            raise CelNotFoundException("Energy Community does not exist")

        installed_power = float(
            data["data"]["potencia_instalada"].replace(",", "."))

        # Send a GET request to the API
        response = requests.get(clients_api_url)
        response.raise_for_status()  # This will raise an exception for non-200 status codes

        # Parse the JSON response
        data = response.json()
        total_contracted_power = sum([float(user["potencia_contratada"].replace(",", "."))
                                      for user in data["data"]])

        return total_contracted_power/installed_power

    except requests.exceptions.RequestException as e:
        # Handle general request exceptions
        raise e
    except CelNotFoundException as e:
        # Handle CelNotFoundException and return a specific HTTP response
        raise HTTPException(status_code=404, detail=str(e))
