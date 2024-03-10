from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health", name="health:health-check",
            tags=["health"],
            response_model=None, status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "ok"}
