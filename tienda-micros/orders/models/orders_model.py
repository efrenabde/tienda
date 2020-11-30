from database import db
import datetime

class OrdersModel(db.Model):
    __tablename__ = "pedidos"

    # Ids
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)

    # Attributes
    id_usuario = db.Column(db.Integer, nullable= False )
    valor_total = db.Column(db.Numeric)
    descuentos = db.Column(db.Numeric)
    # Default
    
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)