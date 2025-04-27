from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar Blueprints después
    from app.controllers.auth_controller import auth_bp
    from app.controllers.turno_controller import turno_bp
    from app.controllers.catalogos_controller import catalogos_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(turno_bp)
    app.register_blueprint(catalogos_bp)

    return app
