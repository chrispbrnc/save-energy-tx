'''
Main Routes

These are the general routes for site
'''
from datetime import datetime
from flask import render_template
from app.main import bp
from app import db


# Set user last seen time
# @bp.before_request
# def before_request():
    # if current_user.is_authenticated:
        # current_user.last_seen = datetime.utcnow()
        # db.session.commit()


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('general/index.html', title='Home')

@bp.route('/faq', methods=['GET'])
def faq():
    return render_template('general/faq.html', title='FAQ')
