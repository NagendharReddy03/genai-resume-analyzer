from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from app.models import User

class RegistrationForm(FlaskForm):
    name     = StringField("Name", validators=[DataRequired(), Length(max=64)])
    email    = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    password2= PasswordField(
        "Repeat Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords must match")]
    )
    submit   = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower()).first()
        if user:
            raise ValidationError("Email already registered.")

class LoginForm(FlaskForm):
    email    = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit   = SubmitField("Login")