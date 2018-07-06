import uuid
import json
from flask import jsonify
from dbHandler import MyDatabase

db = MyDatabase()


class RideRequests:
    """
    class for ride requests
    """

    def __init__(self, ride_id="", passenger="", pickup_point="", destination="",
                 time="", status=False):
        self.request_id = str(uuid.uuid1())
        self.ride_id = ride_id
        self.passenger = passenger
        self.pickup_point = pickup_point
        self.destination = destination
        self.time = time
        self.status = status
        self.errors = []

    def to_json(self):
        """
        json representation of the Ride model
        """
        return {
            'Request id': self.request_id,
            'Ride id': self.ride_id,
            'Passenger': self.passenger,
            'Pickup Point': self.pickup_point,
            'Destination': self.destination,
            'Time': self.time,
            'Status': self.status
        }

    def save_to_db(self):
        # if validate_ride_input(self,  self.passenger, self.pickup_point,
        #                        self.destination, self.time, self.errors):
        sql = "INSERT INTO RequestTable values('{}','{}','{}','{}','{}','{}','{}')".format(
            self.request_id, self.ride_id, self.passenger,
            self.pickup_point, self.destination, self.time, self.status)
        result = db.create_record(sql)
        return result
        # return False

    def modify_request_models(self, status, request_id):
        if validate_ride_input(self, self.passenger, self.pickup_point,
                               self.destination, self.time):
            sql = "UPDATE RequestTable SET status={}'  WHERE request_id = '{}' ".format(
                self.status, self.request_id)
            return db.modify_record(sql)
        return False


def validate_ride_input(self, passenger="", pickup_point="",
                        destination="", time="", errors=[]):
    """ Function to validdate data entered while creating a request """
    result = True
    if len(self.passenger) < 1 or len(self.passenger) > 20 or not self.passenger.isalnum():
        self.errors.append(
            'passenger input must be provided and should be between 4 and 20 characters long and dont use symbols ')

    if len(self.pickup_point) < 1 or len(self.pickup_point):
        self.errors.append(
            'Pick up point input must be provided and should be between 4 and 20 characters long')
        result = False

    if not pickup_point.isalnum():
        result = False

    if len(self.destination) < 1 or len(self.destination) > 20:
        self.errors.append(
            'Destination input must be provided and should be between 4 \
                and 20 characters long')
        result = False
    if not destination.isalnum():
        result = False

    if not self.time:
        self.errors.append(
            'Time input must be provided and should be between 3 and 10 characters long and dont use symbols')
        result = False

    # if self.time.isalnum() is False:
    #     result = False
    return result
