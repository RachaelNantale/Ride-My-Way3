from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal
from app.api import views
from app.api.views import app_bp



app = Flask(__name__)





app.register_blueprint(app_bp)


if __name__ == '__main__':
    app.run(debug=True)