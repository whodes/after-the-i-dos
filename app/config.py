import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite')
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_secret_key")

