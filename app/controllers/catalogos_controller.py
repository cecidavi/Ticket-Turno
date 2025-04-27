from flask import Blueprint

catalogos_bp = Blueprint('catalogos', __name__)

@catalogos_bp.route('/catalogos')
def catalogos_home():
    return "Aquí gestionaremos los catálogos 📚"
