from database import db
import datetime

class ProductsModel(db.Model):
    __tablename__ = "productos"

    # Ids
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)

    # Attributes
    # 1:Admin - 2:Repartidor - 3: Tendero
    id_orden = db.Column(db.Integer, nullable= False )
    nombre_producto = db.Column(db.Integer, default=False)
    valor_unitario = db.Column(db.Numeric)
    cantidad_producto = db.Column(db.Integer, nullable= False )
    # Default
    
    fecha_creacion = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)