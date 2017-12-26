from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email , Length

class SignupForm(Form):
    first_name = StringField('First name', validators =[DataRequired("Please enter your First name!")])
    last_name = StringField('Last name', validators=[DataRequired("Please enter your Last name!")])
    email = StringField('Email', validators=[DataRequired("Please enter your Email!"),Email("Please enter valid email address!")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your Password!"),Length(min=6,message="Passwords must be 6 character or more.")])
    submit = SubmitField('Sign up')
