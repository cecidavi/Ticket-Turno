from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory
from app.models.alumno import Alumno
from app.models.solicitud_turno import SolicitudTurno
from app.models.municipio import Municipio
from app.models.nivel import Nivel
from app.models.asunto import Asunto
from app import db
from app.utils.pdf_generator import generate_ticket_pdf
import os

turno_bp = Blueprint('turno', __name__)

@turno_bp.route('/')
def home():
    return redirect(url_for('turno.solicitar_turno'))

@turno_bp.route('/solicitar-turno', methods=['GET'])
def solicitar_turno():
    municipios = Municipio.query.all()
    niveles = Nivel.query.all()
    asuntos = Asunto.query.all()  # 🔥 Ahora también traemos los asuntos
    return render_template('public/index.html', municipios=municipios, niveles=niveles, asuntos=asuntos)

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

        municipio_nombre = municipio_obj.nombre_mun if municipio_obj else "N/A"
        nivel_nombre = nivel_obj.nivel if nivel_obj else "N/A"
        asunto_nombre = asunto_obj.asunto if asunto_obj else "N/A"

        generate_ticket_pdf(
            curp=curp,
            nombre_completo=nombre_completo,
            turno_municipio=nuevo_turno_numero,
            municipio=municipio_nombre,
            nivel=nivel_nombre,
            asunto=asunto_nombre
        )

        flash(f"Turno registrado exitosamente. Tu número de turno es: {nuevo_turno_numero}", "success")
        return redirect(url_for('turno.turno_exito', curp=curp, turno=nuevo_turno_numero))

    except Exception as e:
        db.session.rollback()
        flash(f"Error al registrar turno: {str(e)}", "danger")
        return redirect(url_for('turno.solicitar_turno'))

@turno_bp.route('/descargar-ticket/<curp>/<int:turno>')
def descargar_ticket(curp, turno):
    try:
        filename = f"{curp}_{turno}.pdf"
        directory = os.path.join(os.getcwd(), 'app', 'static', 'pdf')
        filepath = os.path.join(directory, filename)

        if not os.path.exists(filepath):
            flash("No se encontró el comprobante. Intenta más tarde.", "danger")
            return redirect(url_for('turno.solicitar_turno'))

        return send_from_directory(directory, filename, as_attachment=True)

    except Exception as e:
        flash(f"Error al descargar el comprobante: {str(e)}", "danger")
        return redirect(url_for('turno.solicitar_turno'))

@turno_bp.route('/turno-exito/<curp>/<int:turno>')
def turno_exito(curp, turno):
    return render_template('public/turno_exito.html', curp=curp, turno=turno)

@turno_bp.route('/buscar-turno', methods=['GET', 'POST'])
def buscar_turno():
    if request.method == 'POST':
        curp = request.form.get('curp')

        if not curp:
            flash('Debes ingresar la CURP.', 'warning')
            return redirect(url_for('turno.buscar_turno'))

        solicitud = SolicitudTurno.query.filter_by(curp=curp).first()

        if solicitud:
            return redirect(url_for('turno.editar_turno', id_solicitud=solicitud.id_solicitud))
        else:
            flash('No se encontró el registro.', 'error')
            return redirect(url_for('turno.buscar_turno'))

    return render_template('public/buscar_turno.html')

@turno_bp.route('/editar-turno/<int:id_solicitud>', methods=['GET', 'POST'])
def editar_turno(id_solicitud):
    solicitud = SolicitudTurno.query.get(id_solicitud)
    if not solicitud:
        flash('No se encontró la solicitud.', 'danger')
        return redirect(url_for('turno.buscar_turno'))

    alumno = Alumno.query.get(solicitud.curp)

    if request.method == 'POST':
        solicitud.telefono = request.form.get('telefono')
        solicitud.celular = request.form.get('celular')
        solicitud.correo = request.form.get('correo')

        db.session.commit()
        flash('Datos actualizados correctamente.', 'success')
        return redirect(url_for('turno.solicitar_turno'))

    return render_template('public/editar_turno.html', solicitud=solicitud, alumno=alumno)
