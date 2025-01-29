from fastapi import FastAPI

router = FastAPI()



@router.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


