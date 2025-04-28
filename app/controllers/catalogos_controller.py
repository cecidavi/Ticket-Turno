from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models.municipio import Municipio
from app.models.nivel import Nivel
from app.models.asunto import Asunto
from app.utils.db import db

catalogos_bp = Blueprint('catalogos', __name__)

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

# --- Ruta principal para ver los catálogos ---
@catalogos_bp.route('/admin/catalogos')
@admin_required
def catalogos():
    municipios = Municipio.query.all()
    niveles = Nivel.query.all()
    asuntos = Asunto.query.all()
    return render_template('admin/catalogos.html', municipios=municipios, niveles=niveles, asuntos=asuntos)

# ============================= MUNICIPIOS =============================

@catalogos_bp.route('/admin/catalogos/agregar-municipio', methods=['POST'])
@admin_required
def agregar_municipio():
    nombre = request.form['nombre_mun']
    if nombre:
        nuevo = Municipio(nombre_mun=nombre)
        db.session.add(nuevo)
        db.session.commit()
        flash('Municipio agregado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/editar-municipio/<int:id>', methods=['POST'])
@admin_required
def editar_municipio(id):
    municipio = Municipio.query.get_or_404(id)
    nuevo_nombre = request.form['nombre_mun']
    if nuevo_nombre:
        municipio.nombre_mun = nuevo_nombre
        db.session.commit()
        flash('Municipio editado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/eliminar-municipio/<int:id>', methods=['POST'])
@admin_required
def eliminar_municipio(id):
    municipio = Municipio.query.get_or_404(id)
    db.session.delete(municipio)
    db.session.commit()
    flash('Municipio eliminado correctamente.', 'success')
    return redirect(url_for('catalogos.catalogos'))

# ============================= NIVELES =============================

@catalogos_bp.route('/admin/catalogos/agregar-nivel', methods=['POST'])
@admin_required
def agregar_nivel():
    nombre = request.form['nivel']
    if nombre:
        nuevo = Nivel(nivel=nombre)
        db.session.add(nuevo)
        db.session.commit()
        flash('Nivel agregado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/editar-nivel/<int:id>', methods=['POST'])
@admin_required
def editar_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    nuevo_nombre = request.form['nivel']
    if nuevo_nombre:
        nivel.nivel = nuevo_nombre
        db.session.commit()
        flash('Nivel editado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/eliminar-nivel/<int:id>', methods=['POST'])
@admin_required
def eliminar_nivel(id):
    nivel = Nivel.query.get_or_404(id)
    db.session.delete(nivel)
    db.session.commit()
    flash('Nivel eliminado correctamente.', 'success')
    return redirect(url_for('catalogos.catalogos'))

# ============================= ASUNTOS =============================

@catalogos_bp.route('/admin/catalogos/agregar-asunto', methods=['POST'])
@admin_required
def agregar_asunto():
    nombre = request.form['asunto']
    if nombre:
        nuevo = Asunto(asunto=nombre)
        db.session.add(nuevo)
        db.session.commit()
        flash('Asunto agregado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/editar-asunto/<int:id>', methods=['POST'])
@admin_required
def editar_asunto(id):
    asunto = Asunto.query.get_or_404(id)
    nuevo_nombre = request.form['asunto']
    if nuevo_nombre:
        asunto.asunto = nuevo_nombre
        db.session.commit()
        flash('Asunto editado correctamente.', 'success')
    else:
        flash('El nombre no puede estar vacío.', 'danger')
    return redirect(url_for('catalogos.catalogos'))

@catalogos_bp.route('/admin/catalogos/eliminar-asunto/<int:id>', methods=['POST'])
@admin_required
def eliminar_asunto(id):
    asunto = Asunto.query.get_or_404(id)
    db.session.delete(asunto)
    db.session.commit()
    flash('Asunto eliminado correctamente.', 'success')
    return redirect(url_for('catalogos.catalogos'))
