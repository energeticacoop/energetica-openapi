from fastapi import APIRouter, Path, HTTPException
from models.communities import Community
from pydantic import create_model, TypeAdapter
from dependencies import get_db_query_result

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
