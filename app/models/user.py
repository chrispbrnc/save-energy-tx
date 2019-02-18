import jwt
from datetime import datetime
from flask_login import UserMixin

from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
User model

    username
    email
    password_hash
    about_me
    last_seen
'''
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(120), index=True, unique=True)

    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    address = db.Column(db.String(128))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip_code = db.Column(db.String(10))

    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    stripe_id = db.Column(db.String(64))

    def __repr__(self):
        return '<User {}>'.format(self.username)


