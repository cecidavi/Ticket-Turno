# app/controllers/auth_controller.py

from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from app.models.usuario import Usuario
from app.utils.captcha_validator import validar_captcha
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        captcha_token = request.form.get('g-recaptcha-response')

        if not captcha_token:
            flash('Debes completar el reCAPTCHA.', 'danger')
            return redirect(url_for('auth.login'))

        if not validar_captcha(captcha_token):
            flash('Error de reCAPTCHA. Intenta de nuevo.', 'danger')
            return redirect(url_for('auth.login'))

        user = Usuario.query.filter_by(usuario=usuario).first()
        if user and user.password_hash == password:  # Aquí deberías usar hashing real
            session['admin_id'] = user.id
            flash('Bienvenido, administrador.', 'success')
            return redirect(url_for('auth.admin_panel'))  # 🔥 ahora redirige al panel principal
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('auth.login'))

    site_key = current_app.config['RECAPTCHA_SITE_KEY']
    return render_template('admin/login.html', site_key=site_key)

@auth_bp.route('/admin-panel')
def admin_panel():
    if 'admin_id' not in session:
        flash('Acceso no autorizado. Inicia sesión.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template('admin/admin_panel.html')

@auth_bp.route('/logout')
def logout():
    session.pop('admin_id', None)
    flash('Has cerrado sesión correctamente.', 'info')
    return redirect(url_for('auth.login'))
