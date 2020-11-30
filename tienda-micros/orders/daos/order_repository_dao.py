from database import db
from typing import List
from models.orders_model import OrdersModel
from models.products_model import ProductsModel
import uuid

class OrderRepositoryDao:

    @staticmethod
    def create_order(productos, descuento, valorTotal, idUsuario)-> OrdersModel:
        order = OrdersModel(
            descuentos = descuento,
            valor_total = valorTotal,
            id_usuario = idUsuario
        )
        db.session.add(order)
        db.session.flush()
        orderId = order.id
        db.session.commit()
        
        for product in productos:
            print("Producto"+ str(product))
            product_p = ProductsModel(
                id_orden = orderId,
                nombre_producto = product["nombreProducto"],
                valor_unitario = product["valorUnitario"],
                cantidad_producto = product["cantProducto"]
            )
            db.session.add(product_p)
            db.session.commit()

        return order

    @staticmethod
    def get_order_by_id(orderId) -> OrdersModel:
        return OrdersModel.query.filter(OrdersModel.id == orderId).first()
    
    @staticmethod
    def list_orders() -> List[OrdersModel]:
        return OrdersModel.query.all()

    @staticmethod
    def modify_order_by_id(orderId, descuento, valorTotal, idUsuario, productos) -> OrdersModel:
        order = OrdersModel.query.filter(OrdersModel.id == orderId).first()
        products = ProductsModel.query.filter(ProductsModel.id_orden == orderId).all()
        for i in productos:
            banderaInsert = True
            for j in products:
                if i["eliminarProducto"]:
                    ProductsModel.query.filter(ProductsModel.id_orden == orderId).delete()
                if i["idProducto"] == j.id:
                    j.valor_unitario = i["valorUnitario"]
                    j.cantidad_producto = i["cantProducto"]
                    j.nombre_producto = i["nombreProducto"]
                    db.session.commit()
                    banderaInsert = False
            if banderaInsert:
                new_product = ProductsModel(
                    id_orden = orderId,
                    nombre_producto = i["nombreProducto"],
                    valor_unitario = i["valorUnitario"],
                    cantidad_producto = i["cantProducto"]
                )
                db.session.add(new_product)
                db.session.commit()
        order.descuentos = descuento
        order.valor_total = valorTotal
        db.session.commit()