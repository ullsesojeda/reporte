from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    nombre = db.Column(db.String(100))
    rol = db.Column(db.String(20))


class Gasto(db.Model):
    __tablename__ = "gastos"

    id = db.Column(db.Integer, primary_key=True)

    fecha = db.Column(db.Date, nullable=False)

    pagado_a = db.Column(db.String(200))

    concepto = db.Column(db.String(200))

    observaciones = db.Column(db.Text)

    responsable = db.Column(db.String(50))

    importe = db.Column(db.Float)

    fecha_registro = db.Column(
        db.DateTime,
        default=datetime.now
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuarios.id')
    )