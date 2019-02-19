'''
Email utilities
'''
from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail

# Send off email async so it doesn't block the main thread
def send_async_email(app, msg):
    with app.app_context():
        mail.send_email(
            to_email=msg['to_email'],
            subject=msg['subject'],
            from_email=msg['from_email'],
            html=msg['html'],
            text=msg['text'])


# Send an email using flask_mail
def send_email(subject, sender, recipients, text_body, html_body):
    msg = {
        'subject': subject,
        'to_email': recipients,
        'from_email': sender,
        'html': html_body,
        'text': text_body,
    }
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
