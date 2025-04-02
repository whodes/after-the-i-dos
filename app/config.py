"""Configuration settings for the Flask application."""

import os
from dataclasses import dataclass


@dataclass
class Config:
    """Base configuration class."""

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///db.sqlite"
    )
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_secret_key")
