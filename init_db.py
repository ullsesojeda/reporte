from flask import Flask
from config import Config
from models import db, Usuario
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():

    os.makedirs("database", exist_ok=True)

    db.create_all()

    admin = Usuario.query.filter_by(
        usuario='admin'
    ).first()

    if not admin:

        admin = Usuario(
            usuario='admin',
            password=generate_password_hash('admin123'),
            nombre='Administrador',
            rol='Administrador'
        )

        db.session.add(admin)
        db.session.commit()

        print("Administrador creado")
        print("Usuario: admin")
        print("Contraseña: admin123")

    else:
        print("La base ya existe.")