from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CURRENCY_API_KEY: str
    CURRENCY_BASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
