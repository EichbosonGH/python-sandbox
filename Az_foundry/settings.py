"""Holds configs for the app."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App Config Parameters."""

    model_config = SettingsConfigDict(
        env_file=".env",
    )

    scope: str = "https://cognitiveservices.azure.com/.default"
    endpoint: str = "https://aif-msai.services.ai.azure.com/openai/v1"
    model: str = "gpt-5.6-luna"
    api_key: str = Field(init=False)

settings = Settings()