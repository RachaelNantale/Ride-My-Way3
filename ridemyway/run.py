from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal
import api
from api.views import views
from api import  views
app = Flask(__name__, static_url_path="")



app.register_blueprint(views)


if __name__ == '__main__':
    app.run(debug=True)