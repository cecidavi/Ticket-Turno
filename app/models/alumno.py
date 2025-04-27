from app import db

class Alumno(db.Model):
    __tablename__ = 'alumno'

    curp = db.Column(db.String(18), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    paterno = db.Column(db.String(50), nullable=False)
    materno = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Alumno {self.curp}>'
