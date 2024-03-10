from fastapi import HTTPException, APIRouter, status, BackgroundTasks
from loguru import logger
import asyncio

router = APIRouter()


def perform_health_check():
    # Add your health checks here
    health_status = True
    if health_status:
        logger.info("Health check passed: status okay")
    else:
        logger.error("Health check failed: status not okay")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Health check failed")
    return status


async def health_check_task():
    while True:
        perform_health_check()
        await asyncio.sleep(60)


async def health_startup_event():
    logger.info("Starting health check task")
    asyncio.create_task(health_check_task())


@router.get("",
            name="health:health-check",
            tags=["health"],
            response_model=None,
            status_code=status.HTTP_200_OK)
async def health_check(background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_health_check)
    return {"status": "ok"}
