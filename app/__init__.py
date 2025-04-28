# app/__init__.py

from flask import Flask
from flask_migrate import Migrate
from app.utils.db import db  

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints
    from app.controllers.auth_controller import auth_bp
    from app.controllers.turno_controller import turno_bp
    from app.controllers.catalogos_controller import catalogos_bp
    from app.controllers.dashboard_controller import dashboard_bp
    from app.controllers.api_controller import api_bp  

    app.register_blueprint(auth_bp)
    app.register_blueprint(turno_bp)
    app.register_blueprint(catalogos_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)


    return app
