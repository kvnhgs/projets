from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Class formulaire utilisateurs
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prenom = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    sexe = db.Column(db.String(1), nullable=False)
    pseudo = db.Column(db.String(50), unique=True, nullable=False)

# Class log
class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    datetime = db.Column(db.DateTime)
    ticker = db.Column(db.String(10))
    company = db.Column(db.String(50))
    price_at_datetime = db.Column(db.String(20))