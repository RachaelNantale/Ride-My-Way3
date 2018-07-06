from flask import Flask, Blueprint, jsonify
from instance.config import app_config
from .api.views.views import app_bp
from .api.views.user_views import app_bps
from .api.views.requests_views import app_register
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)




def resource_not_found(error):
    return jsonify({"message": error.description}), 404


def create_app(config_module):
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = 'sup3rsecr3t'
    jwt = JWTManager(app)

    app.config.from_object(app_config[config_module])
    app.register_blueprint(app_bp)
    app.register_blueprint(app_bps)
    app.register_blueprint(app_register)
    app.register_error_handler(404, resource_not_found)
    return app
