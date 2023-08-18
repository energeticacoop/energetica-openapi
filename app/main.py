from fastapi import FastAPI
from routers import users

description = """
⚡ Energética Coop's API for cooperative users, clients and services ⚡
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users, both cooperative members and clients",
    },
    {
        "name": "root",
        "description": "A useless endpoint with a message",
    },
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="Energética Coop API",
    version="0.0.1",
    description=description,
    openapi_tags=tags_metadata
)

app.include_router(users.router, tags=["users"])


@app.get("/", tags=["root"])
async def read_main():
    return {"msg": "Greetings from Energética Coop!"}
