from flask import Flask, jsonify, abort, make_response, Blueprint
from flask_restful import Api, Resource, reqparse, fields, marshal
# from run import app
# app = Flask(__name__, static_url_path="")
app_bp = Blueprint('app', __name__)
api = Api(app_bp)
RIDES = [
    {
    "driver": "Amos Quito",
    "Pickup Point": "kanjokya",
    "Destination": "Bukoto street",
    "Time": "7:00pm",
    "done":False
},
 {
	
    "driver": "Amos Quito",
    "Pickup Point": "kanjokya",
    "Destination": "Bukoto street",
    "Time": "7:00pm",
    "done":True
}
]

RIDES_fields = {
    'driver': fields.String,
    'Pickup Point': fields.String,
    'Destination': fields.String,
    'Time':fields.String,
    'done':fields.Boolean,
    'uri': fields.Url('app.ride')
}


class RideofferList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, required=True,
                                   location='json')
        self.reqparse.add_argument('Pickup Point', type=str, required=True,
                                   help='No Pickup Point provided',
                                   location='json')
        self.reqparse.add_argument('Destination', type=str, required=True,
                                   location='json')
        self.reqparse.add_argument('Time', type=str, required=True,
                                   location='json')
        super(RideofferList, self).__init__()

    def get(self):
        return {'rides': [marshal(task, RIDES_fields) for task in RIDES]}

    def post(self):
        args = self.reqparse.parse_args()
        ride = {
            'rideId': RIDES[-1]['rideId'] + 1,
            'driver': args['driver'],
            'Pickup Point': args['Pickup Point'],
            'Destination': args['Destination'],
            'Time': args['Time'],
            'done': False
        }
        RIDES.append(ride)
        return {'ride': marshal(ride, RIDES_fields)}, 201
        


class Rideoffer(Resource):
    

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('driver', type=str, location='json')
        self.reqparse.add_argument('Pickup Point', type=str, location='json')
        self.reqparse.add_argument('Destination', type=str, location='json')
        self.reqparse.add_argument('Time', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(Rideoffer, self).__init__()

    def get(self, rideId):
        # tasky = []
        # for task in RIDES:
        #     if task["rideId"] == rideId:
        #         tasky.append(task)
        
        task = [task for task in RIDES if task['rideId'] == rideId]

        if len(task) == 0:
            abort(404)
        return {'ride': marshal(task[0], RIDES_fields)}

    def put(self, rideId):
        task = [task for task in RIDES if task['rideId'] == id]
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                task[k] = v
        return {'ride': marshal(task, RIDES_fields)}

    def delete(self, rideId):
        task = [task for task in RIDES if task['rideId'] == id]
        if len(task) == 0:
            abort(404)
        RIDES.remove(task[0])
        return {'result': True}


api.add_resource(RideofferList, '/api/v1/rides', endpoint='rides')
api.add_resource(Rideoffer, '/api/v1/rides/<int:rideId>', endpoint='ride')

# if __name__ == '__main__':
#     app.run(debug=True)

