'''
Energy Saver application

This file manages the creation of the Flask application
'''
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

import os

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sendgrid import SendGrid
import stripe

from app.config import Config

'''
App features

SQLAlchemy
Login Manager
Mail
Stripe
'''

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access that page.'
login.login_message_category = 'warning'
mail = SendGrid()


'''
Create App

This function sets up the Flask app and returns it. Call create_app to create an instance of the
application.

In this function the blueprints are imported and set up. Debugging messages are also set up to report
in the Heroku dashboard
'''
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    stripe.api_key = app.config['STRIPE_SECRET_KEY']

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], subject='Energy Saver Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if app.config['LOG_TO_STDOUT']:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)
            app.logger.addHandler(stream_handler)
        else:
            if not os.path.exists('logs'):
                    os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/site.log', maxBytes=10240,
                                               backupCount=10)
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Energy Saver App startup')

    return app

import app.models
