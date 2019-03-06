from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
import stripe
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models.user import User
from app.auth.email import send_password_reset_email, send_verification_email


# Login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is logged in, skip the login page and go to the profile page
    if current_user.is_authenticated:
        return redirect(url_for('user.profile'))
    form = LoginForm()

    # If the form was submitted and is validated
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Check if the user exists and that the password is correct
        if user is None or not user.check_password(form.password.data):
            # If not, show error
            flash('Invalid email or password', 'warning')
            return redirect(url_for('auth.login'))
        # Otherwise log the user in
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('user.profile'))

    # If the page is a GET request, send the loging template
    return render_template('auth/login.html', title='Log in', form=form)

# Logout route
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Register
@bp.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is logged in, skip the register page and go to the profile page
    if current_user.is_authenticated:
        return redirect
    form = RegistrationForm()

    # If the form was submitted and is validated
    if form.validate_on_submit():
        # Create user
        u = User()
        u.username = form.email.data
        u.email = form.email.data
        u.firstname = form.firstname.data
        u.lastname = form.lastname.data
        u.address = form.address.data
        u.city = form.city.data
        u.state = form.state.data
        u.zip_code = form.zip_code.data
        u.phone_number = form.phone_number.data
        u.set_password(form.password.data)
        u.verified = False
        u.active_sub = False
        u.subscription = ""

        # Create stripe user
        customer = stripe.Customer.create(email=u.email)
        u.stripe_id = customer.id


        # Save user to DB
        db.session.add(u)
        db.session.commit()

        # Send verification email to user
        send_verification_email(u)

        # Send user a success message
        flash('Success! Check your email for a verification link', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title='Register', form=form)

@bp.route('/resend-verify', methods=['GET'])
def resend_verify():
    if not current_user.verified:
        send_verification_email(current_user)
        flash("Check your email for the verification link", "info")
    return redirect(url_for('user.profile'))

# Verify Email
@bp.route('/verify-email/<token>', methods=['GET', 'POST'])
def verify_email(token):
    # If the user is logged in, skip the reset password page
    if current_user.is_authenticated and current_user.verified:
        return redirect(url_for('user.profile'))
    u = User.verify_email(token)

    # If don't find the user, redirect home
    if not u:
        return redirect(url_for('main.index'))

    # Verify the user
    u.verified = True
    db.session.commit()

    flash('Success! Your account is now verified', 'success')
    return redirect(url_for('user.profile'))


# Reset Password Request
@bp.route('/reset-password', methods=['GET', 'POST'])
def reset_password_request():
    # If the user is logged in, skip the reset password page
    if current_user.is_authenticated:
        return redirect(url_for('user.profile'))
    form = ResetPasswordRequestForm()

    # If the form was submitted and is validated
    if form.validate_on_submit():
        u = User.query.filter_by(email=form.email.data).first()
        # If we find the user, send them the password reset email
        if u:
            send_password_reset_email(u)
        flash('Success! Check your email for instructions on the next steps for resetting your password', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/reset-password-request.html', title='Reset Password', form=form)

# Reset Password with token
@bp.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # If the user is logged in, skip the reset password page
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    u = User.verify_reset_password(token)

    # If don't find the user, redirect home
    if not u:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()

    # If the form was submitted and is validated, set the new password
    if form.validate_on_submit():
        u.set_password(form.password.data)
        db.session.commit()
        flash('Success! Your password has been reset.', 'success')
        return redirect(url_for('auth.login'))

    return redirect(url_for('main.index'))
