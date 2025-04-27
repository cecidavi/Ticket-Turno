from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from app.forms.login_form import LoginForm
from app.models.usuario import Usuario
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        usuario = form.usuario.data
        password = form.password.data

        # Buscar el usuario en la base de datos
        user = Usuario.query.filter_by(usuario=usuario).first()

        if user and user.password_hash == password:  # Aún no hasheado
            session['usuario'] = user.usuario
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('turno.dashboard'))  # Redirigir a dashboard después
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('admin/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    flash('Sesión cerrada correctamente.', 'success')
    return redirect(url_for('auth.login'))
