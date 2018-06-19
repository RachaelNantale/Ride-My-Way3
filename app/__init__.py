from flask import Flask, Blueprint
from instance.config import app_config
from .api.views import app_bp


def create_app(config_module):
    app = Flask(__name__)

    app.config.from_object(app_config[config_module])
    app.register_blueprint(app_bp)
    return app