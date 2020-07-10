from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FlaskBlog.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')
    accept = BooleanField('I agree with terms and condition', validators=[DataRequired()])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user: #if user exist
            raise ValidationError('Username is taken')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email: #if email exist
            raise ValidationError('This email already exist')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
   
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user: #if user exist
                raise ValidationError('Username is the same')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email: #if email exist
                raise ValidationError('This email is the same')


class QuestionForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # email = current_user.email
    question = TextField('Write your question here', validators=[DataRequired()])
    submit = SubmitField('Post')
