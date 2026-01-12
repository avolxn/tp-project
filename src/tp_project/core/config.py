from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CURRENCY_API_KEY: str
    CURRENCY_BASE_URL: str

    REDIS_URL: str = "redis://localhost:6379"
    CACHE_TTL: int = 3600

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
