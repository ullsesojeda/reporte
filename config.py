import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Base de datos local o en Render
if os.path.exists("/montesion/gastos"):
    DATABASE_PATH = "/montesion/gastos/gastos.db"
else:
    DATABASE_PATH = os.path.join(BASE_DIR, "database", "gastos.db")

class Config:
    SECRET_KEY = "cambia_esta_clave_super_secreta"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False