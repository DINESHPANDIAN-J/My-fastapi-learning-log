from pydantic import BaseSettings, Field
from typing import Optional, List

class Settings(BaseSettings):
    app_name: str = "FastAPI_mini_project_1",
    debug:bool = False,
    version:str = "1.0.0",
    allowed_hosts:List[str]

    class config:
        env_file = ".env"

settings = Settings()

