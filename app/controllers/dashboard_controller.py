# app/controllers/dashboard_controller.py

from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app.models.solicitud_turno import SolicitudTurno
from app.models.municipio import Municipio
from app.utils.db import db
from sqlalchemy import func
from datetime import datetime, timedelta

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

# --- Dashboard con gráfico y listado ---
@dashboard_bp.route('/admin/dashboard', methods=['GET'])
@admin_required
def dashboard():
    municipios = Municipio.query.all()
    municipio_id = request.args.get('municipio', type=int)

    solicitudes_query = SolicitudTurno.query
    if municipio_id:
        solicitudes_query = solicitudes_query.filter_by(cve_mun=municipio_id)

    # Filtrar turnos pendientes
    solicitudes = solicitudes_query.filter_by(id_estatus=1).all()

    # Datos para la gráfica
    if municipio_id:
        pendientes = SolicitudTurno.query.filter_by(id_estatus=1, cve_mun=municipio_id).count()
        resueltos = SolicitudTurno.query.filter_by(id_estatus=2, cve_mun=municipio_id).count()
    else:
        pendientes = SolicitudTurno.query.filter_by(id_estatus=1).count()
        resueltos = SolicitudTurno.query.filter_by(id_estatus=2).count()

    total = pendientes + resueltos

    # --- Automáticamente cambiar a Resuelto si pasaron 1 minuto ---
    ahora = datetime.now()
    hace_un_minuto = ahora - timedelta(minutes=1)

    auto_resueltos = SolicitudTurno.query.filter(
        SolicitudTurno.id_estatus == 1,
        SolicitudTurno.fecha_registro <= hace_un_minuto
    ).all()

    for solicitud in auto_resueltos:
        solicitud.id_estatus = 2  # Cambiar a "Resuelto"

    if auto_resueltos:
        db.session.commit()

    return render_template(
        'admin/dashboard.html',
        municipios=municipios,
        solicitudes=solicitudes,
        pendientes=pendientes,
        resueltos=resueltos,
        total=total,
        municipio_id=municipio_id
    )

# --- Ruta para cambiar manualmente estatus ---
@dashboard_bp.route('/admin/cambiar-estatus/<int:id>', methods=['POST'])
@admin_required
def cambiar_estatus(id):
    solicitud = SolicitudTurno.query.get_or_404(id)
    solicitud.id_estatus = 2  # 2 = Resuelto
    db.session.commit()
    flash('Turno actualizado a Resuelto.', 'success')
    return redirect(url_for('dashboard.dashboard'))
