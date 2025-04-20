from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    cdn_host: str
    redirect_ratio: int = 3

    class Config:
        env_file = ".env"


settings = Settings()
