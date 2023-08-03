from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    joyful = db.Column(db.Boolean, default=False)
    imglink = db.Column(db.String(150))

def get_all_users():
    return User.query.all()

def get_joyful_users():
    return User.query.filter_by(joyful=True).all()

def get_unjoyful_users():
    return User.query.filter_by(joyful=False).all()
