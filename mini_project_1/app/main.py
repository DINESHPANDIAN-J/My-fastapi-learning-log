from fastapi import FastAPI
from mini_project_1.app.core.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)

@app.get('/config_check')
def read_config():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "version": settings.version,
        "allowed_hosts": settings.allowed_hosts
    }


