# app/config.py

import os

class Config:
    # Clave secreta de Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecreto123'

    # Conexión a la base de datos
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://cecilio:ceci1282@localhost/ticket_turno'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de reCAPTCHA
    RECAPTCHA_SITE_KEY = '6Lcn4yYrAAAAAK9FXj8A4_Iu5cGvIdhWo3rWhP-T'
    RECAPTCHA_SECRET_KEY = '6Lcn4yYrAAAAAKOSEwlUv6Il0Aq76R2aS9FvdUYz'
