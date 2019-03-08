from flask import render_template, current_app
from app.email import send_email

# Contact Us Email
def send_contactus_email(user, issue, message):
    send_email('[Energy Savers] Issue from Customer',
        sender=current_app.config['ADMINS'][0],
        recipients=current_app.config['ADMINS'][1],
        text_body=render_template('email/contact/contact.txt',
            user=user, issue=issue, message=message),
        html_body=render_template('email/contact/contact.html',
            user=user, issue=issue, message=message))
