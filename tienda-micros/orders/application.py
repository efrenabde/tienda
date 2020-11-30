from flask import Flask, jsonify
from database import db
#from blueprints.continuous_resource_blueprint import create_continuous_resource_blueprint
from blueprints.orders_blueprint import create_orders_blueprint
import os
import logging

logger = logging.getLogger(__name__)

def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Register continuous resource blueprints
   
    app.register_blueprint(
        create_orders_blueprint(
            blueprint_name="OrdersBlueprint",
            resource_type="Order",
            resource_prefix="orders"
        ),
        url_prefix='/api'
    )

    return app


if __name__=="__main__":
    app = create_app(db_uri="sqlite:///red.db")
    app.run("0.0.0.0", port=7000, debug=True)
