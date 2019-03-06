from flask import render_template, current_app
from app.email import send_email

# Subscription Removal Request
def send_removal_request_email(user):
    id = user.stripe_id
    send_email('[Energy Savers] Payment Removal Request',
        sender=current_app.config['ADMINS'][0],
        recipients=current_app.config['ADMINS'][1],
        text_body=render_template('email/removal_request/removal_request.txt',
            user=user, id=id),
        html_body=render_template('email/removal_request/removal_request.html',
            user=user, id=id))
