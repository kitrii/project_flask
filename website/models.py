from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique =True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))

class Application(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique =True)
    phone = db.Column(db.String(255), unique =True)
    org = db.Column(db.String(255), unique =True)
    cv = db.Column(db.String(10000), unique =True)








