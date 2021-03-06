'''
Payments Routes

These are the general routes for managing payments
'''
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user
from app.payments import bp
from app.payments.email import send_removal_request_email
from app import db
import stripe


@bp.route('/add', methods=['GET', 'POST'])
def add():
    email = request.form['stripeEmail']
    token = request.form['stripeToken']
    try:
        stripe.Customer.modify(current_user.stripe_id, source=token)
        current_user.active_sub = True
        db.session.commit()
        flash('Successfully added card to account', 'success')
        return redirect(url_for('profile.profile'))
    except stripe.error.CardError:
        flash('There was an issue adding the card', 'danger')
        return redirect(url_for('main.index'))

@bp.route('/edit', methods=['GET', 'POST'])
def edit():
    email = request.form['stripeEmail']
    token = request.form['stripeToken']
    try:
        stripe.Customer.modify(current_user.stripe_id, source=token)
        flash('Successfully edited card', 'success')
        return redirect(url_for('profile.profile'))
    except:
        flash('There was an issue editing the card', 'danger')
        return redirect(url_for('main.index'))

@bp.route('/remove', methods=['POST'])
def remove():
    # Send email to admin to request a removal of payment
    send_removal_request_email(current_user)
    flash("The request to remove your subscription has been sent, a response will be sent to your email shortly.", "success")
    return redirect(url_for('profile.profile'))
