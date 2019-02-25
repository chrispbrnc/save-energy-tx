from flask import render_template, current_app
from app.email import send_email

# Email Verification Email
def send_moreinfo_email(email):
    send_email('[Energy Savers] Information',
        sender=current_app.config['ADMINS'][0],
        recipients=email,
        text_body=render_template('email/more_info/more_info.txt'),
        html_body=render_template('email/more_info/more_info.html'))
