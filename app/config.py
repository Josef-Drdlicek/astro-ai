import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
    APP_NAME = "Astro AI"
    DEFAULT_LOCALE = os.getenv("DEFAULT_LOCALE", "cs")
