from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, RadioField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'username'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'password'})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={'placeholder': 'ex: JohnnyAppleseed'})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'ex: JohnnyAppleseed@yahoo.com'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'come up with a strong password!'})
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')], render_kw={'placeholder': 'repeat password'})
    dob = DateField('Date of Birth', format='%m/%d/%Y', validators=[DataRequired()], render_kw={'placeholder': 'format: mm/dd/yyyy'})
    cc_number = StringField('Credit Card Number', validators=[DataRequired()], render_kw={'placeholder': '################'})
    cc_company = RadioField('Credit Card Company', choices=[('Visa', 'Visa'), ('Mastercard', 'Mastercard')],
                            validators=[DataRequired()])
    expiration = DateField('Card Expiration', format='%m/%Y', validators=[DataRequired()], render_kw={'placeholder': 'format: mm/yyyy'})
    cvc = IntegerField('Security Code', validators=[DataRequired()], render_kw={'placeholder': '###'})

    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


