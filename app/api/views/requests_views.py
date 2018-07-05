from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.ride import RideOffers
from app.api.models.user import User
from app.api.models.request import RideRequests
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)
import uuid
from dbHandler import MyDatabase

app_register = Blueprint('app_register', __name__)
api = Api(app_register)

db = MyDatabase()
requestss = RideRequests()


class RequestofferList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('passenger', type=str, required=True,
                                   help='No passenger provided',
                                   location='json')
        self.reqparse.add_argument('pickup_point', type=str, required=True,
                                   help='No Pickup Point provided',
                                   location='json')
        self.reqparse.add_argument('Destination', type=str, required=True,
                                   help='No Destination provided',
                                   location='json')
        self.reqparse.add_argument('Time', type=str, required=True,
                                   help='No Time provided',
                                   location='json')
        super(RequestofferList, self).__init__()

    @jwt_required
    def get(self, ride_id):
        _id = str(uuid.uuid1())
        result = db.fetch_all_requests(ride_id)
        if result is not None:
            return jsonify({'result': result})
        else:
            return jsonify({'message': 'You have no requests'})

    @jwt_required
    def post(self, ride_id):
        if ride_id:
            request = RideRequests(ride_id=ride_id)
            print(request)
            args = self.reqparse.parse_args()
            request = RideRequests(
                ride_id,
                args['passenger'],
                args['pickup_point'],
                args['Destination'],
                args['Time'], False)
            print(request)
            request.save_to_db()
            return make_response(jsonify({
                'message': 'A request to join this ride has been sent'
            }), 201)
        return make_response(jsonify({
            'message': 'No request'
        }), 400)


class Requestoffer(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, location='json')
        self.reqparse.add_argument('pickup_point', type=str, location='json')
        self.reqparse.add_argument('destination', type=str, location='json')
        self.reqparse.add_argument('time', type=str, location='json')
        self.reqparse.add_argument('status', type=bool, location='json')
        super(Requestoffer, self).__init__()

    @jwt_required
    def get(self, request_id):
        result = db.fetch_one_request(request_id)

        if len(result) < 1:

            return jsonify({'result': result})
        else:
            return jsonify({'message': 'You have no requests'}), 400

    @jwt_required
    def put(self, ride_id, request_id):

        args = self.reqparse.parse_args()

        status = args['status']

        if status == 1:
            message = 'Approved request'
            status_code = 200
            status_msg = 'Success'
            
            request = RideRequests(ride_id=ride_id)
            
            request.modify_request_models(status, request_id)
            



            return make_response(jsonify({'Message': message,
                                          'status': status_msg}), status_code)
        else:
            message = 'Reject request.'
            status_code = 200
            status_msg = 'success'

        return make_response(jsonify({'Message': message,
                                      'status': status_msg}), status_code)


api.add_resource(
    Requestoffer, '/api/v1/rides/<string:ride_id>/requests/<string:request_id>')

api.add_resource(RequestofferList, '/api/v1/rides/<string:ride_id>/requests')
# api.add_resource(Requestoffer, '/api/v1/rides/<string:ride_id>/requests/<string:request_id>')
