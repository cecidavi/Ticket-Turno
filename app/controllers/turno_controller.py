# app/controllers/turno_controller.py

from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory, session
from app.models.alumno import Alumno
from app.models.solicitud_turno import SolicitudTurno
from app.models.municipio import Municipio
from app.models.nivel import Nivel
from app.models.asunto import Asunto
from app import db
from app.utils.pdf_generator import generate_ticket_pdf
import os

turno_bp = Blueprint('turno', __name__)

# --- Página principal ---
@turno_bp.route('/')
def home():
    return redirect(url_for('turno.solicitar_turno'))

# --- Formulario público para solicitar turno ---
@turno_bp.route('/solicitar-turno', methods=['GET'])
def solicitar_turno():
    municipios = Municipio.query.all()
    niveles = Nivel.query.all()
    asuntos = Asunto.query.all()
    return render_template('public/index.html', municipios=municipios, niveles=niveles, asuntos=asuntos)

# --- Registrar un turno ---
@turno_bp.route('/registrar-turno', methods=['POST'])
def registrar_turno():
    try:
        nombre_completo = request.form['nombre_completo']
        curp = request.form['curp']
        nombre = request.form['nombre']
        paterno = request.form['paterno']
        materno = request.form['materno']
        telefono = request.form['telefono']
        celular = request.form['celular']
        correo = request.form['correo']
        nivel = request.form['nivel']
        municipio = request.form['municipio']
        asunto = request.form['asunto']

        if not curp or not nombre or not paterno or not materno:
            flash("Faltan datos obligatorios.", "danger")
            return redirect(url_for('turno.solicitar_turno'))

        alumno_existente = Alumno.query.filter_by(curp=curp).first()
        if not alumno_existente:
            nuevo_alumno = Alumno(
                curp=curp,
                nombre=nombre,
                paterno=paterno,
                materno=materno
            )
            db.session.add(nuevo_alumno)

        total_turnos = SolicitudTurno.query.filter_by(cve_mun=municipio).count()
        nuevo_turno_numero = total_turnos + 1

        nueva_solicitud = SolicitudTurno(
            curp=curp,
            cve_mun=int(municipio),
            cve_nivel=int(nivel),
            id_asunto=int(asunto),
            telefono=telefono,
            celular=celular,
            correo=correo,
            turno_municipio=nuevo_turno_numero
        )
        db.session.add(nueva_solicitud)
        db.session.commit()

        municipio_obj = Municipio.query.get(int(municipio))
        nivel_obj = Nivel.query.get(int(nivel))
        asunto_obj = Asunto.query.get(int(asunto))

        generate_ticket_pdf(
            curp=curp,
            nombre_completo=nombre_completo,
            turno_municipio=nuevo_turno_numero,
            municipio=municipio_obj.nombre_mun,
            nivel=nivel_obj.nivel,
            asunto=asunto_obj.asunto
        )

        flash(f"Turno registrado exitosamente. Tu número de turno es: {nuevo_turno_numero}", "success")
        return redirect(url_for('turno.turno_exito', curp=curp, turno=nuevo_turno_numero))

    except Exception as e:
        db.session.rollback()
        flash(f"Error al registrar turno: {str(e)}", "danger")
        return redirect(url_for('turno.solicitar_turno'))

# --- Descargar PDF del ticket ---
@turno_bp.route('/descargar-ticket/<curp>/<int:turno>')
def descargar_ticket(curp, turno):
    try:
        filename = f"{curp}_{turno}.pdf"
        directory = os.path.join(os.getcwd(), 'app', 'static', 'pdf')
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        flash(f"Error al descargar el comprobante: {str(e)}", "danger")
        return redirect(url_for('turno.solicitar_turno'))

# --- Página de éxito al generar turno ---
@turno_bp.route('/turno-exito/<curp>/<int:turno>')
def turno_exito(curp, turno):
    return render_template('public/turno_exito.html', curp=curp, turno=turno)

# --- Buscar registro por CURP (público) ---
@turno_bp.route('/buscar-turno', methods=['GET', 'POST'])
def buscar_turno():
    if request.method == 'POST':
        curp = request.form['curp'].strip().upper()
        if not curp:
            flash('Debes ingresar un CURP.', 'warning')
            return redirect(url_for('turno.buscar_turno'))

        solicitudes = SolicitudTurno.query.filter_by(curp=curp).all()

        if not solicitudes:
            flash('No se encontraron registros para ese CURP.', 'danger')
            return redirect(url_for('turno.buscar_turno'))

        return render_template('public/alumno_panel.html', curp=curp, solicitudes=solicitudes)

    return render_template('public/buscar_turno.html')

# --- Editar datos del turno ---
@turno_bp.route('/editar-turno/<int:id_solicitud>', methods=['GET', 'POST'])
def editar_turno(id_solicitud):
    solicitud = SolicitudTurno.query.get_or_404(id_solicitud)
    alumno = Alumno.query.filter_by(curp=solicitud.curp).first()

    if request.method == 'POST':
        # Actualizar datos
        alumno.nombre = request.form['nombre']
        alumno.paterno = request.form['paterno']
        alumno.materno = request.form['materno']
        solicitud.telefono = request.form['telefono']
        solicitud.celular = request.form['celular']
        solicitud.correo = request.form['correo']

        db.session.commit()
        flash('Datos actualizados correctamente.', 'success')
        return redirect(url_for('turno.buscar_turno'))

    return render_template('public/editar_turno.html', solicitud=solicitud, alumno=alumno)
