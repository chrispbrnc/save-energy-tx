from flask import render_template, current_app
from app.email import send_email

# Email Verification Email
def send_moreinfo_email(email):
    send_email('[Energy Savers] Information',
        sender=current_app.config['ADMINS'][0],
        recipients=email,
        text_body=render_template('email/more_info/more_info.txt'),
        html_body=render_template('email/more_info/more_info.html'))

    send_email('[Energy Savers] Information Request',
        sender=current_app.config['ADMINS'][0],
        recipients=app.config['ADMINS'][1],
        text_body=render_template('email/more_info/more_info_admin.txt'),
        html_body=render_template('email/more_info/more_info_admin.html'))
