from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["root"])
async def root():
    return {"msg": "Greetings from Energética Coop!"}
