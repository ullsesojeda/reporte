import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'cambia_esta_clave_super_secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR,
        'database',
        'gastos.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False