from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models.user import User

class EditProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip_code = StringField('Zip Code', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    submit = SubmitField('Submit')
