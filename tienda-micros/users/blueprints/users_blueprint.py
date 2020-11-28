from flask import Blueprint, jsonify, request, abort
from serialisers.alchemy_encoder import AlchemyEncoder
import json
import datetime
import logging

from daos.user_repository_dao import UserRepositoryDao

logger = logging.getLogger(__name__)

def create_users_blueprint(blueprint_name: str, resource_type: str, resource_prefix: str) -> Blueprint:
    """
    blueprint_name: name of the blueprint, used by Flask for routing
    resource_type: name of the specific type of interval resource, such as boy bay or payload bay
    resource_prefix: the plural resource to be used in the api endpoint, such as bot_bay, resulting in "/bot_bays"
    """
    blueprint = Blueprint(blueprint_name, __name__)

    @blueprint.route(f'/{resource_prefix}', methods=["POST"])
    def create_user():
        logger.info("Creando usuario")
        user= UserRepositoryDao.create_user(tipo=request.get_json(force=True)['tipo'],nombre=request.get_json(force=True)['nombre'])
        return json.dumps(user, cls=AlchemyEncoder), 201
    
    @blueprint.route(f'/{resource_prefix}/<user_id>', methods=["GET"])
    def get_resource(user_id):
        logger.info(f"Consulta de Usuario {user_id}")
        user = UserRepositoryDao.get_user_by_id(userId=user_id)
        return json.dumps(user, cls=AlchemyEncoder), 200

    return blueprint
