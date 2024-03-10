from fastapi import APIRouter

from app.api.routes import semantic_search, health

router = APIRouter()
router.include_router(health.router,
                      tags=['health'],
                      prefix='/health')

router.include_router(semantic_search.router,
                      tags=['semantic_search'],
                      prefix='/semantic_search')
