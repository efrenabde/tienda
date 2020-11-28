from database import db
from typing import List
from models.users_model import UsersModel
import uuid

class UserRepositoryDao:

    @staticmethod
    def create_user(tipo,nombre)-> UsersModel:
        user = UsersModel(
            tipo_usuario= tipo,
            nombre_usuario= nombre
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user_by_id(userId) -> UsersModel:
        return UsersModel.query.filter(UsersModel.id == userId).first()