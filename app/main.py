from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import users
from routers import utils

description = """
⚡ Energética Coop's API for cooperative users, clients and services ⚡
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users, both cooperative members and clients",
    },
    {
        "name": "utils",
        "description": "Varied endpoints for special operations in PV studies",
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

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, tags=["users"])
app.include_router(utils.router, tags=["utils"])


@app.get("/", tags=["root"])
async def read_main():
    return {"msg": "Greetings from Energética Coop!"}
