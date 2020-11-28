from database import db
import datetime

class OrdersModel(db.Model):
    __tablename__ = "pedidos"

    # Ids
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)

    # Attributes
    # 1:Admin - 2:Repartidor - 3: Tendero
    nom_producto = db.Column(db.Integer, default=False)
    valor_producto = db.Column(db.Numeric)
    cant_producto = db.Column(db.Integer, nullable= False )
    # Default
    
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)