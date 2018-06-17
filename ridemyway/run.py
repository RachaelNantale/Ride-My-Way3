from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

RIDES = {
    'rideoffer1': {'ride_offer':'from Kampala to Mukono'},
    'rideoffer2': {'ride_offer':'from Kampala to Bweyogerere'},
    'rideoffer3': {'ride_offer':'from Kampala to Bushenyi'},
    }

def abort_if_rideoffer_doesnt_exist(rideoffer_id):
    if rideoffer_id not in RIDES:
        abort(404, message = "Rideoffer {} doesn't exist".format(rideoffer_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

#class shows a single ride offer and you delete a single ride offer
class Rideoffer(Resource):
    def get(self,rideoffer_id):
        abort_if_rideoffer_doesnt_exist(rideoffer_id)
        return RIDES[rideoffer_id]

    def delete(self, rideoffer_id):
        abort_if_rideoffer_doesnt_exist(rideoffer_id)
        del RIDES[rideoffer_id]
        return '', 204

    def put(self, rideoffer_id):
        args = parser.parse_args()
        task = {'task':args['task']}
        RIDES[rideoffer_id] = task
        return task, 201


# shows a list of all ride offers and lets you create new ones
class RideofferList(Resource):
    def get(self):
        return RIDES

    def post(self):
        args = parser.parse_args()
        rideoffer_id = int(max(RIDES.keys()).lstrip('rideoffer')) + 1
        rideoffer_id = 'rideoffer%i' % rideoffer_id
        RIDES[rideoffer_id] = {'task':args['task']}
        return RIDES[rideoffer_id],201

    # set up Api resource routing here
api.add_resource(Rideoffer, '/rides/<rideoffer_id>')
api.add_resource(RideofferList,  '/rides')  


if __name__ == '__main__':
    app.run(debug=True)
