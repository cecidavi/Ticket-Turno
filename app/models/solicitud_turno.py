from app import db

class SolicitudTurno(db.Model):
    __tablename__ = 'solicitud_turno'

    id_solicitud = db.Column(db.Integer, primary_key=True)
    curp = db.Column(db.String(18), db.ForeignKey('alumno.curp'), nullable=False)
    cve_mun = db.Column(db.Integer, nullable=False)
    cve_nivel = db.Column(db.Integer, nullable=False)
    id_asunto = db.Column(db.Integer, nullable=False)
    id_estatus = db.Column(db.Integer, default=1)  # 1 = Pendiente
    telefono = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    correo = db.Column(db.String(100))
    fecha_registro = db.Column(db.DateTime, server_default=db.func.now())
    turno_municipio = db.Column(db.Integer, nullable=False)  # Número de turno asignado por municipio

    def __repr__(self):
        return f'<SolicitudTurno {self.id_solicitud}>'
