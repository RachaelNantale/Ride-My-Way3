from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields
from app.api.models.ride import RideOffers
from app.api.models.user import User
# from app.utility import ValidateRideData
app_bp = Blueprint('app', __name__)
api = Api(app_bp)


RIDES = []


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

    def get(self):
        json_rides = [ride.to_json() for ride in RIDES]
        if len(json_rides) == 0:
            return make_response(jsonify({'message': 'sorry no rides yet'}))
        return make_response(jsonify(json_rides), 200)

    def post(self):
        args = self.reqparse.parse_args()
        ride = RideOffers(args['driver'], args['pickup_point'],
                          args['Destination'], args['Time'], False)

        if ride.save_to_db():
            message = 'Ride Created Successfuly'
            status_code = 201
            status_msg = 'Success'

        else:
            message = 'Ride Not Created.'
            if len(ride.errors) > 0:
                message = ' '.join(ride.errors)
            status_code = 400
            status_msg = 'Fail'

        return make_response(jsonify({'Message': message,
                                      'status': status_msg}), status_code)


class Rideoffer(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, location='json')
        self.reqparse.add_argument('pickup_point', type=str, location='json')
        self.reqparse.add_argument('Destination', type=str, location='json')
        self.reqparse.add_argument('Time', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(Rideoffer, self).__init__()

    def get(self, id):
        for ride in RIDES:
            if ride.get_id() == id:

                return make_response(jsonify(
                    ride.to_json()
                ), 200)
        return make_response(jsonify({"message": "Ride not found."}), 404)

    def put(self, id):
        task = [ride for ride in RIDES if ride.get_id() == id]
        if len(task) == 0:
            abort(404)
        ride = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if k is not 'id':
                setattr(ride, k, v)
                print(k)
                print(v)
                # print(ride)
                print('---------------------')
        return make_response(jsonify(ride.to_json()), 201)

    def delete(self, id):
        task = [ride for ride in RIDES if ride.get_id() == id]
        if len(task) == 0:
            abort(404)
        RIDES.remove(task[0])
        return {'result': True}


api.add_resource(RideofferList, '/api/v1/rides')
api.add_resource(Rideoffer, '/api/v1/rides/<string:id>')
