from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models.usuario import Usuario
from app.utils.db import db

auth_bp = Blueprint('auth', __name__)

# --- Login ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']

        admin = Usuario.query.filter_by(usuario=usuario, password_hash=password).first()

        if admin:
            session['admin_id'] = admin.id
            flash('Bienvenido administrador.', 'success')
            return redirect(url_for('auth.admin_panel'))  # 👈 Redirige al panel admin
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
            return redirect(url_for('auth.login'))

    return render_template('admin/login.html')

# --- Logout ---
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente.', 'success')
    return redirect(url_for('auth.login'))

# --- Panel administrador ---
@auth_bp.route('/admin-panel')
def admin_panel():
    if 'admin_id' not in session:
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('auth.login'))
    return render_template('admin/admin_panel.html')
