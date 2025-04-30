from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email"),
            Email(message="Must be a valid email address")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter a password")]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message="Please confirm your password"),
            EqualTo('password', message='Passwords must match')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Please enter your email"),
            Email(message="Must be a valid email address")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(message="Please enter your password")]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')