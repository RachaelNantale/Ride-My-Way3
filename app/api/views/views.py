from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse
from app.api.models.ride import RideOffers
from app.api.models.user import User
import uuid
from flask_jwt_extended import (jwt_required, create_access_token)
from dbHandler import MyDatabase

app_bp = Blueprint('app', __name__)
api = Api(app_bp)

db = MyDatabase()


class RideofferList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, required=True,
                                   help='No driver provided',
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
        super(RideofferList, self).__init__()

    @jwt_required
    def get(self):
        _id = str(uuid.uuid1())
        result = db.fetch_all_rides(_id)
        if result is not None:
            return jsonify({'result': result})
        else:
            return jsonify({'message': 'You have no requests'})

    @jwt_required
    def post(self):
        args = self.reqparse.parse_args()
        ride = RideOffers(args['driver'], args['pickup_point'],
                          args['Destination'], args['Time'], False)
        try:
            ride.save_to_db()
            message = 'Ride Created Successfuly'
            status_code = 201
            status_msg = 'Success'

            return make_response(jsonify({'Message': message,
                                          'status': status_msg}), status_code)

        except Exception:
            message = 'Ride Not Created.'
            if len(ride.errors) > 0:
                message = ride.errors
            status_code = 400
            status_msg = 'Fail'

            return make_response(jsonify({'Message': message,
                                          'status': status_msg}), status_code)


class Rideoffer(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, location='json')
        self.reqparse.add_argument('pickup_point', type=str, location='json')
        self.reqparse.add_argument('destination', type=str, location='json')
        self.reqparse.add_argument('time', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(Rideoffer, self).__init__()

    @jwt_required
    def get(self, id):
        result = db.fetch_one_ride(id)

        if result is not None:

            return jsonify({'result': result})
        else:
            return jsonify({'message': 'You have no requests'})

    @jwt_required
    def put(self, id):
        args = self.reqparse.parse_args()
        ride = RideOffers(args['driver'], args['pickup_point'],
                          args['destination'], args['time'], False)

        if ride.modify_ride_models(args['driver'], args['pickup_point'],
                                   args['destination'], args['time'],
                                   False, id):
            print(ride)
            message = 'Modified requests'
            status_code = 201
            status_msg = 'Success'

        else:
            message = 'Sorry could not modify request.'
            if len(ride.errors) > 0:
                message = ride.errors
            status_code = 400
            status_msg = 'Fail'

        return make_response(jsonify({'Message': message,
                                      'status': status_msg}), status_code)

    @jwt_required
    def delete(self, id):
        _id = str(uuid.uuid1())
        db.delete_record(_id)
        return jsonify({'result': True})


api.add_resource(RideofferList, '/api/v1/rides')
api.add_resource(Rideoffer, '/api/v1/rides/<string:id>')
