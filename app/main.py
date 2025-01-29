import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import openData, users, communities, utils, root

description = """
⚡ Energética Coop's API for cooperative users, clients and services ⚡
"""

tags_metadata = [
    {
        "name": "open data",
        "description": "Open Data for the cooperative",
    },
    {
        "name": "users",
        "description": "Operations with users, both cooperative members and clients",
    },
    {
        "name": "communities",
        "description": "Operations with energy communities",
    },
    {
        "name": "utils",
        "description": "Varied endpoints for special operations in PV studies",
    },
    {
        "name": "root",
        "description": "A greeting message",
    },
    {
        "name": "health",
        "description": "Endpoints for checking the API's health and system status",
    },
]

app = FastAPI(
    openapi_url="/api/v1/openapi.json",
    title="Energética Coop API",
    version="0.0.3"
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

app.include_router(openData.router, tags=["open data"])
app.include_router(users.router, tags=["users"])
app.include_router(communities.router, tags=["communities"])
app.include_router(utils.router, tags=["utils"])
app.include_router(root.router, tags=["root"])
app.include_router(root.router, tags=["health"])

# For local testing
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
