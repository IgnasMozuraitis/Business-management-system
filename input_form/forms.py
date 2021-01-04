from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo
import email_validator

class ClientInputForm(FlaskForm):
    client_name = StringField('Kliento vardas', validators = [DataRequired()])
    sumbit = SubmitField('Įrašyti')


class RegistrationForm(FlaskForm):
    username = StringField('Vartotojo vardas',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('El. paštas',
                        validators=[DataRequired()])
    password = PasswordField('Slaptažodis', validators=[DataRequired()])
    confirm_password = PasswordField('Patvirtinkite slaptažodį',
                                     validators=[DataRequired(), EqualTo('Slaptažodis')])
    submit = SubmitField('Prisijungti')


# class LoginForm(FlaskForm):
#     email = StringField('El. paštas',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Slaptažodis', validators=[DataRequired()])
#     remember = BooleanField('Prisiminti mane')
#     submit = SubmitField('Prisijungti')