from flask import render_template, current_app
from app.email import send_email

# Email Verification Email
def send_verification_email(user):
    token = user.get_verify_email_token()
    send_email('[Energy Savers] Email Verification',
        sender=current_app.config['ADMINS'][0],
        recipients=user.email,
        text_body=render_template('email/verification/verification.txt',
            user=user, token=token),
        html_body=render_template('email/verification/verification.html',
            user=user, token=token))

# Reset Password Email
def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Energy Savers] Reset Your Password',
        sender=current_app.config['ADMINS'][0],
        recipients=user.email,
        text_body=render_template('email/forgot-password/forgot-password.txt',
            user=user, token=token),
        html_body=render_template('email/forgot-password/forgot-password.html',
            user=user, token=token))
