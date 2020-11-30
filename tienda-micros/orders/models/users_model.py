from database import db
import datetime

class UsersModel(db.Model):
    __tablename__ = "usuarios"

    # Ids
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Attributes
    # 1:Admin - 2:Repartidor - 3: Tendero
    tipo_usuario = db.Column(db.Integer, default=False)
    nombre_usuario = db.Column(db.String(20))
    # Default
    pass_usuario = db.Column(db.String(20), nullable= False, default='1234' )
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)