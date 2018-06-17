from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal
from api import views
from api.views import app






if __name__ == '__main__':
    app.run(debug=True)