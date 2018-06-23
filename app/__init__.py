from flask import Flask, Blueprint
from instance.config import app_config
from .api.views.views import app_bp
from .api.views.user_views import app_bps


def create_app(config_module):
    app = Flask(__name__)

    app.config.from_object(app_config[config_module])
    app.register_blueprint(app_bp)
    app.register_blueprint(app_bps)

    return app
