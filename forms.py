from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, validators
from wtforms.fields import EmailField, TextAreaField, RadioField, PasswordField, IntegerField

def mi_Validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError("El campo no tiene datos")

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='long de campo 4 min and 10 max')
        ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')
        ])
    apaterno = StringField('Apaterno')
    amaterno = StringField('Amaterno', [mi_Validacion])
    email = EmailField('Correo')
    contrasenia = PasswordField('Contrasenia')
    numero = IntegerField('numero')
    campo = IntegerField('campo')

class LoginForm(Form):
    username = StringField('usuario', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='long de campo 4 min and 10 max')
        ])
    password = PasswordField('contraseña', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message='long de campo 4 min and 10 max')
        ])

class transForm(Form):
    ingles = StringField('Inglés', [mi_Validacion])
    espaniol = StringField('Español', [mi_Validacion])
    trad = StringField("Escribe la palabra")#,[mi_Validacion])
    
