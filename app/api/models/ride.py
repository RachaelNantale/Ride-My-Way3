import uuid
import json
from flask import jsonify
from dbHandler import MyDatabase
# from app.utility import validate_ride_input


db = MyDatabase()


class RideOffers:
    """
    class for ride offers
    """

    def __init__(self, driver, pickup_point, destination, time, done):
        self.id = str(uuid.uuid1())
        self.driver = driver.strip()
        self.pickup_point = pickup_point.strip()
        self.destination = destination.strip()
        self.time = time.strip()
        self.done = done
        self.errors = []

    def to_json(self):
        """
        json representation of the Ride model
        """
        return {
            'id': self.id,
            'Driver': self.driver,
            'Pickup Point': self.pickup_point,
            'Destination': self.destination,
            'Time': self.time,
            'done': self.done
        }

    def save_to_db(self):
        if validate_ride_input(self, self.driver, self.pickup_point,
                               self.destination, self.time):
            print('================')
            sql = "INSERT INTO RideTable values('{}','{}','{}','{}','{}','{}')".format(
                self.id, self.driver, self.pickup_point, self.destination,
                self.time, self.done)
            result = db.create_record(sql)
            return result

        return False

    # def modify_ride_models(self, driver, pickup_point, destination, time, done, id):
    #     if validate_ride_input(self, self.driver, self.pickup_point,
    #                            self.destination, self.time, self.errors):
    #         sql = "UPDATE RideTable SET self.driver = '{}', self.pickup_point = '{}', self.destination = '{}', self.time = '{}'  WHERE self.id = '{}' ".format(
    #             self.driver, self.pickup_point, self.destination,
    #             self.time, self.done, self.id)
    #         return db.modify_ride(sql)
    #     return False


def validate_ride_input(self, driver, pickup_point, destination, time):
    """ Function to validdate data entered while creating a request """
    result = True
    if len(self.driver) < 1 or len(self.driver) > 20 or not self.driver.isalnum():
        self.errors.append(
            'Driver input must be provided and should be between 4 and 20 characters long and dont use symbols ')

    if len(self.pickup_point) < 1 or len(self.pickup_point):
        self.errors.append(
            'Pick up point input must be provided and should be between 4 and 20 characters long')
        result = False

    if pickup_point.isalnum():
        result = False

    if len(self.driver) < 1 or len(self.driver) > 20:
        self.errors.append(
            'Destination input must be provided and should be between 4 \
                and 20 characters long')
        result = False
    if destination.isalnum():
        result = False

    if len(self.driver) < 1 or len(self.driver) > 7:
        self.errors.append(
            'Time input must be provided and should be between 3 and 10 characters long and dont use symbols')
        result = False

    if time.isalnum():
        result = False
    return result


class RideRequests:
    """
    class for ride requests
    """

    def __init__(self, passenger, pickup_point, destination, time):
        self.id = uuid.uuid4().hex
        self.passenger = passenger
        self.pickup_point = pickup_point
        self.destination = destination
        self.time = time

    def get_id(self):
        return self.id

    def get_passenger(self):
        return self.passenger

    def get_pickup_point(self):
        return self.pickup_point

    def get_destination(self):
        return self.destination

    def get_time(self):
        return self.time

    def to_json(self):
        """
        json representation of the Ride model
        """
        return {
            'id': self.id,
            'Passenger': self.passenger,
            'Pickup Point': self.pickup_point,
            'Destination': self.destination,
            'Time': self.time
        }
