"""Flask application factory for the app module."""

from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes import routes


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(routes)

    return app
