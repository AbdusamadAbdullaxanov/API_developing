from pydantic import BaseSettings


class Settings(BaseSettings):
    user: str = "postgres"
    password: str = "postgresql"
    host: str = "localhost"
    database: str = "FastAPI"
    port: str = "5432"
    access_key: str = "Private token"
    algorithm: str = "HS256"
    expire_time: int = 60

    class Config:
        env_file = '.env'


settings = Settings()
