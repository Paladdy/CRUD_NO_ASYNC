from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str # Тип данных URL до Бд

    model_config = SettingsConfigDict(
        env_file='.env', # Сам файл до БД
        extra='ignore' # Игнор доп параметров
    )

Config = Settings()