from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    """Model untuk data buku"""
    __tablename__ = 'books'

    isbn = db.Column(db.String(20), primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(300))
    year = db.Column(db.Integer)
    publisher = db.Column(db.String(300))


class User(db.Model):
    """Model untuk data user"""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(500))
    age = db.Column(db.Integer)


class Rating(db.Model):
    """Model untuk data rating"""
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    isbn = db.Column(db.String(20), db.ForeignKey('books.isbn'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
