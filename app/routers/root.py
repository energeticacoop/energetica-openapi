from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["root"])
async def read_main():
    return {"msg": "Greetings from Energética Coop!"}
