
from flask_wtf import FlaskForm, form
from wtforms import StringField, SubmitField, IntegerField, SelectField, EmailField
from wtforms.validators import Required, Length, EqualTo


class ClientInputForm(FlaskForm):
    company_name = StringField('Įmonės pavadinimas', validators = [Required()])
    manager = StringField('Įmonės vadovas')
    #client_type = SelectField(u'Group', coerce=int)
    mob_phone_number = IntegerField('Mob. Tel. Nr.')
    email = EmailField('El. paštas')
    country = StringField('Šalis')
    comments = StringField('Komentarai')
    """
    website = URLField('Tinklapis (www)')
    Traceback (most recent call last):
  File "app.py", line 2, in <module>
    from input_form import app
  File "/home/ubuntupc/solarteka/input_form/__init__.py", line 13, in <module>
    from input_form import routes
  File "/home/ubuntupc/solarteka/input_form/routes.py", line 8, in <module>
    from .forms import ClientInputForm
  File "/home/ubuntupc/solarteka/input_form/forms.py", line 2, in <module>
    from wtforms import StringField, URLField, SubmitField, IntegerField, SelectField, EmailField
    ImportError: cannot import name 'URLField' from 'wtforms' (/home/ubuntupc/solarteka/.venv/lib/python3.8/site-packages/wtforms/__init__.py)
    """
    website = StringField('Tinklapis (www)')
    sumbit = SubmitField('Išsaugoti')


# class RegistrationForm(FlaskForm):
#     username = StringField('Vartotojo vardas',
#                            validators=[DataRequired(), Length(min=2, max=20)])
#     email = StringField('El. paštas',
#                         validators=[DataRequired()])
#     password = PasswordField('Slaptažodis', validators=[DataRequired()])
#     confirm_password = PasswordField('Patvirtinkite slaptažodį',
#                                      validators=[DataRequired(), EqualTo('Slaptažodis')])
#     submit = SubmitField('Prisijungti')


# class LoginForm(FlaskForm):
#     email = StringField('El. paštas',
#                         validators=[DataRequired(), Email()])
#     password = PasswordField('Slaptažodis', validators=[DataRequired()])
#     remember = BooleanField('Prisiminti mane')
#     submit = SubmitField('Prisijungti')