from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField

class CadastroForm(FlaskForm):
    usuario = StringField(label='username')
    email = StringField(label='email')
    senha1 = PasswordField(label='senha')
    senha2 = PasswordField(label='confirmacao de senha')
    submit = SubmitField(label='Cadastrar')



# class RegistrationForm(Form):
#     username = StringField('Username', [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])
#     confirm = PasswordField('Repeat Password')
#     accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])