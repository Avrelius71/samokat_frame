from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    user_email: str
    user_password: str
    admin_email: str
    admin_password: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

settings = Settings()