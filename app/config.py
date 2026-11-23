from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    environment: str
    database_url: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# A global instance is created that can be imported throughout the entire project
settings = Settings()







"""
# ..... check & hit terminal
 python -c "from app.config import settings; print(settings.app_name)"

# ........ Check data base connected 
python -c "from app.database import engine; conn = engine.connect(); print('Database connected successfully!'); conn.close()"
"""
