# app/controllers/api_controller.py

from flask import Blueprint, jsonify, request
from app.models.solicitud_turno import SolicitudTurno
from app.models.municipio import Municipio
from app.models.nivel import Nivel
from app.models.asunto import Asunto

api_bp = Blueprint('api', __name__, url_prefix='/api')

# ----------------- Turnos -----------------

@api_bp.route('/solicitudes', methods=['GET'])
def listar_solicitudes():
    municipio_id = request.args.get('municipio_id', type=int)

    if municipio_id:
        solicitudes = SolicitudTurno.query.filter_by(cve_mun=municipio_id).all()
    else:
        solicitudes = SolicitudTurno.query.all()

    data = []
    for s in solicitudes:
        data.append({
            'id_solicitud': s.id_solicitud,
            'curp': s.curp,
            'municipio_id': s.cve_mun,
            'nivel_id': s.cve_nivel,
            'asunto_id': s.id_asunto,
            'telefono': s.telefono,
            'celular': s.celular,
            'correo': s.correo,
            'turno_municipio': s.turno_municipio,
            'estatus_id': s.id_estatus
        })

    return jsonify(data)

# ----------------- Municipios -----------------

@api_bp.route('/municipios', methods=['GET'])
def listar_municipios():
    municipios = Municipio.query.all()
    data = [{'id': m.cve_mun, 'nombre': m.nombre_mun} for m in municipios]
    return jsonify(data)

# ----------------- Niveles -----------------

@api_bp.route('/niveles', methods=['GET'])
def listar_niveles():
    niveles = Nivel.query.all()
    data = [{'id': n.cve_nivel, 'nombre': n.nivel} for n in niveles]
    return jsonify(data)

# ----------------- Asuntos -----------------

@api_bp.route('/asuntos', methods=['GET'])
def listar_asuntos():
    asuntos = Asunto.query.all()
    data = [{'id': a.id_asunto, 'nombre': a.asunto} for a in asuntos]
    return jsonify(data)
