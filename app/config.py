import os

class Config:
    """Flask application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sistem-rekomendasi-perpustakaan-2024')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///library.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
