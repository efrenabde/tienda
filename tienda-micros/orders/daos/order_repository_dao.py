from database import db
from typing import List
from models.orders_model import OrdersModel
import uuid

class OrderRepositoryDao:

    @staticmethod
    def create_order(nomProducto,valorProducto,cantProducto)-> OrdersModel:
        order = OrdersModel(
            nom_producto = nomProducto,
            valor_producto = valorProducto,
            cant_producto = cantProducto
        )
        db.session.add(order)
        db.session.commit()
        return user

    @staticmethod
    def get_order_by_id(orderId) -> OrdersModel:
        return OrdersModel.query.filter(OrdersModel.id == orderId).first()
