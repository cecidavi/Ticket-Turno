from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(), Length(min=4, max=30)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=4, max=30)])
    submit = SubmitField('Iniciar Sesión')
