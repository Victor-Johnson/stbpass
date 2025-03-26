from Fastapi import APIRouter

router = APIRouter()

@router.get("/pass/all-houses")
async def 