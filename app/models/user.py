import jwt
from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
User model

    email
    username

    firstname
    lastname

    address
    city
    state
    zip_code

    password_hash
    last_seen

    verified

    stripe_id
'''
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(120), index=True, unique=True)

    verified = db.Column(db.Boolean)

    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))

    address = db.Column(db.String(128))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    zip_code = db.Column(db.Integer)

    password_hash = db.Column(db.String(128))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    stripe_id = db.Column(db.String(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?id=identicon&s={}'.format(digest, size)


    # Generate the reset password token
    def get_reset_password_token(self, expires_in=600):
        data = {
            'reset_password': self.id,
            'exp': time() + expires_in,
        }
        return jwt.encode(data, current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    # Generate the verify email token
    def get_verify_email_token(self, expires_in=600):
        data = {
            'verify_email': self.id,
            'exp': time() + expires_in
        }
        return jwt.encode(data, current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    # Returns a user from the id in the JWT
    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    # Returns a user from the id in the JWT
    @staticmethod
    def verify_email(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['verify_email']
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return '<User {}>'.format(self.username)
