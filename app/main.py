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
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="Energética Coop API",
    version="0.0.1",
    description=description,
)

app.include_router(users.router)
