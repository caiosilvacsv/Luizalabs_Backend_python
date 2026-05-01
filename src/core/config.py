
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  DATABASE_URL: str
  SECRET : str
  ALGORITHM : str
  ENVIRONMENT : str = "development"
  
  model_config = SettingsConfigDict(
    env_file = ".env",
    env_file_encoding = "utf-8",
    extra="ignore"
  )

settings = Settings()