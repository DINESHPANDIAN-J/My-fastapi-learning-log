from fastapi import FastAPI
from intermediate_level.api.routes import router as api_router
from intermediate_level.core.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug, version=settings.version)
app.include_router(api_router, prefix="/api", tags=["API"])

@app.get("/config-check")
def read_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "version": settings.version,
        "database_url": settings.database_url
    }