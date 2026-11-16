from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    user_email: str = "test_user@example.com"
    user_password: str = "test_password"
    admin_email: str = "admin@example.com"
    admin_password: str = "admin_password"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

settings = Settings()