from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.solicitud_turno import SolicitudTurno

dashboard_bp = Blueprint('dashboard', __name__)

# --- Proteger rutas solo para admins ---
def admin_required(func):
    from functools import wraps
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if 'admin_id' not in session:
            flash('Acceso denegado. Inicia sesión como administrador.', 'danger')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return decorated_view

# --- Ruta para ver el Dashboard ---
@dashboard_bp.route('/admin/dashboard')
@admin_required
def dashboard():
    pendientes = SolicitudTurno.query.filter_by(id_estatus=1).count()
    resueltos = SolicitudTurno.query.filter_by(id_estatus=2).count()

    return render_template('admin/dashboard.html', pendientes=pendientes, resueltos=resueltos)
