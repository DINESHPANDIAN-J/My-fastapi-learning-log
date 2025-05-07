from fastapi import FastAPI
from intermediate_level.api.routes import router as api_router

app = FastAPI(title="Dinesh's API World!", version="1.0.0")
app.include_router(api_router, prefix="/api", tags=["API"])