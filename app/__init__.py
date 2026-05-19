from flask import Flask
from .config import Config
from .database import db
from .recommender import HybridRecommender

# Global recommender instance
recommender = HybridRecommender()


def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Load recommendation models
    recommender.load_models()

    # Register routes
    from .routes import main
    app.register_blueprint(main)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
