#users_blueprint_test.py
import pytest
import blueprints.users_blueprint

def create_user_test():
    blueP=  users_blueprint.create_users_blueprint(blueprint_name="users", resource_type="users", resource_prefix="/user")
    print("setting up", blueP.create_user())

def create_users_blueprint_test():
    users_blueprint.create_users_blueprint(blueprint_name="users", resource_type="users", resource_prefix="/user")
    obj =users_blueprint.create_users()
    obj.code=201
    assert obj.code==201
