from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    app_name:str = "FastAPI App"
    debug: bool = False
    version: str = "1.0.0"
    database_url: str 

    class Config:
        env_file = ".env" #load from .env file

# Global settings object
settings = Settings()