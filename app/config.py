import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecreto123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://cecilio:ceci1282@localhost/ticket_turno'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
