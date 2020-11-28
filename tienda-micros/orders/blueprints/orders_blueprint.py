from flask import Blueprint, jsonify, request, abort
from serialisers.alchemy_encoder import AlchemyEncoder
#from daos.continuous_resource_dao import ContinuousResourceDao
import json
import datetime
import logging

from daos.order_repository_dao import OrderRepositoryDao

logger = logging.getLogger(__name__)

def create_orders_blueprint(blueprint_name: str, resource_type: str, resource_prefix: str) -> Blueprint:
    """
    blueprint_name: name of the blueprint, used by Flask for routing
    resource_type: name of the specific type of interval resource, such as boy bay or payload bay
    resource_prefix: the plural resource to be used in the api endpoint, such as bot_bay, resulting in "/bot_bays"
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route(f'/{resource_prefix}', methods=["POST"])
    def create_order():
        logger.info("Creando usuario")
        order= OrderRepositoryDao.create_order(nomProducto = request.get_json(force=True)['nombreProducto'],
                                                valorProducto= request.get_json(force=True)['valorProducto'],
                                                cantProducto=request.get_json(force=True)['cantidadProducto'])
        return json.dumps(order, cls=AlchemyEncoder), 201
    
    @blueprint.route(f'/{resource_prefix}/<order_id>', methods=["GET"])
    def get_order(order_id):
        logger.info(f"Consulta de Usuario {order_id}")
        order = OrderRepositoryDao.get_order_by_id(orderId=order_id)
        return json.dumps(order, cls=AlchemyEncoder), 200

    return blueprint
