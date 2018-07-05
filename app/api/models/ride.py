import uuid
import json
from flask import jsonify
from dbHandler import MyDatabase


db = MyDatabase()


class RideOffers:
    """
    class for ride offers
    """

    def __init__(self, driver, pickup_point, destination, time, done):
        self.id = str(uuid.uuid1())
        self.driver = driver
        self.pickup_point = pickup_point
        self.destination = destination
        self.time = time
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
            sql = "INSERT INTO RideTable values('{}','{}','{}','{}','{}','{}')RETURNING id".format(
                self.id, self.driver, self.pickup_point, self.destination,
                self.time, self.done)
            result = db.create_login(sql)
            return result
        return False

    def modify_ride_models(self, driver, pickup_point,
                           destination, time, done, id):
        if validate_ride_input(self, self.driver, self.pickup_point,
                               self.destination, self.time):
            sql = "UPDATE RideTable SET driver = '{}', pickup_point = '{}', destination = '{}', time = '{}'  WHERE id = '{}' ".format(
                self.driver, self.pickup_point, self.destination,
                self.time, self.done, self.id)
            return db.modify_record(sql)
        return False


def validate_ride_input(self, driver, pickup_point, destination, time):
    """ Function to validdate data entered while creating a request """
    result = True
    if len(self.driver) < 1 or len(self.driver) > 40 or self.driver.isalnum() is False:
        self.errors.append(
            'Driver input must be provided and should be between 4 and 20 characters long and dont use symbols ')
        result = False
    if len(self.pickup_point) < 1 or len(self.pickup_point) > 30 or pickup_point.isalnum() is False:
        self.errors.append(
            'Pick up point input must be provided and should be between 4 and 20 characters long')
        result = False

    if not self.destination or len(self.destination) > 20 or destination.isalnum() is False:
        self.errors.append(
            'Destination input must be provided and should be between 4 \
                and 20 characters long')
        result = False

    if not self.time or len(self.time) > 7 or time.isalnum is False:
        self.errors.append(
            'Time input must be provided and should be between 3 and 10 characters long and dont use symbols')
        result = False
    return True