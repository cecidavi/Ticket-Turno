from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.models.solicitud_turno import SolicitudTurno
from app.models.municipio import Municipio

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

# --- Dashboard con filtro por municipio ---
@dashboard_bp.route('/admin/dashboard', methods=['GET'])
@admin_required
def dashboard():
    municipios = Municipio.query.all()

    municipio_id = request.args.get('municipio', type=int)
    if municipio_id:
        pendientes = SolicitudTurno.query.filter_by(id_estatus=1, cve_mun=municipio_id).count()
        resueltos = SolicitudTurno.query.filter_by(id_estatus=2, cve_mun=municipio_id).count()
    else:
        pendientes = SolicitudTurno.query.filter_by(id_estatus=1).count()
        resueltos = SolicitudTurno.query.filter_by(id_estatus=2).count()

    total = pendientes + resueltos

    return render_template(
        'admin/dashboard.html',
        municipios=municipios,
        pendientes=pendientes,
        resueltos=resueltos,
        total=total,
        municipio_id=municipio_id
    )
