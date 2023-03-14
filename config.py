from pydantic import BaseSettings

class Settings(BaseSettings):
    username: str
    password: str
    hostname: str
    database: str
    port: int
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()