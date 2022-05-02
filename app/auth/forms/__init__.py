from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class login_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    submit = SubmitField("Login")


class register_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ])

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ])
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")
    submit = SubmitField("Register")


class profile_form(FlaskForm):
    file = FileField()
    about = TextAreaField('About', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")

    submit = SubmitField()


class user_edit_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)],
                          description="Please add information about yourself")
    is_admin = BooleanField('Admin', render_kw={'value':'1'})
    submit = SubmitField("Update")


class security_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="You can change your email address")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),

    ], description="Create a password ")
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")

    submit = SubmitField("Update")


