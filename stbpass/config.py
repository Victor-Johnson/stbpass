from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import Optional 

class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra="ignore")


class GlobalConfig(BaseConfig):
    DATABASE_URL : Optional[str] = None 
    DB_FORCE_ROLL_BACK = False 