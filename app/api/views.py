from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal
from app.api.models import RideOffers, User
app_bp = Blueprint('app', __name__)
api = Api(app_bp)
# RIDES = [
#     {
# 	"rideId": 1,
#     "driver": "Amos Quito",
#     "Pickup Point": "kanjokya",
#     "Destination": "Bukoto street",
#     "Time": "7:00pm",
#     "done":False
# },
#  {
# 	"rideId": 2,
# "driver": "Amos Quito",
# "pickup_point": "kanjokya",
# "Destination": "Bukoto street",
# "Time": "7:00pm",
# "done":True
# }
# ]

RIDES_fields = {
    'driver': fields.String,
    'pickup_point': fields.String,
    'destination': fields.String,
    'time': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('app.ride')
}

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
        # return {'rides': [marshal(task, RIDES_fields) for task in RIDES]}
        # print(RIDES)
        
         for ride in RIDES:
            print(RIDES)
            print('+++++++++++++++++++++BODA============')

            if ride.get_id() == id:
                ride = {
                    "id": ride["id"],
                    "driver": ride['driver'],
                    "pickup_point": ride['pickup_point'],
                    "Destination": ride['Destination'],
                    "Time": ride['Time'],
                    "done": ride['done']

                }
                print(RIDES)
                print('++++++++++++++++++++GUY+============')
                RIDES.append(ride)
                response = {'Ride Offer': ride}
                print(RIDES)
                print('+++++++++++++++++HERMAN++++============')
                
                return make_response(response), 200

    def post(self):
        args = self.reqparse.parse_args()
        ride = RideOffers(args['driver'], args['pickup_point'],
                          args['Destination'], args['Time'], False)
        RIDES.append(ride)
        # response = {'Ride offers': ride}
        return make_response(jsonify({
            'message': 'Ride Offer Succesfully Created',
            'status': 'success'
        }), 201)


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
        # tasky = []
        # for task in RIDES:
        #     if task["rideId"] == rideId:
        #         tasky.append(task)

        task = [task for task in RIDES if task['id'] == id]

        if len(task) == 0:
            abort(404)
            return make_response(jsonify({
                'message': 'Ride Offer Succesfully Created',
                'status': 'success'
            }), 201)
        # return {'ride': marshal(task[0], RIDES_fields)}

    def put(self, id):
        task = [task for task in RIDES if task['id'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'ride': marshal(task, RIDES_fields)}

    def delete(self, id):
        task = [task for task in RIDES if task['id'] == id]
        if len(task) == 0:
            abort(404)
        RIDES.remove(task[0])
        return {'result': True}


api.add_resource(RideofferList, '/api/v1/rides', endpoint='rides')
api.add_resource(Rideoffer, '/api/v1/rides/<int:id>', endpoint='ride')
