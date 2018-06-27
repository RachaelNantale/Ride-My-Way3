import uuid
import json
from flask import jsonify


class RideOffers:
    """
    class for ride offers
    """

    def __init__(self, driver, pickup_point, destination, time, done):
        self.id = uuid.uuid4().hex
        self.driver = driver
        self.pickup_point = pickup_point
        self.destination = destination
        self.time = time
        self.done = done

    def get_id(self):
        return self.id

    def get_driver(self):
        return self.driver

    def get_pickup_point(self):
        return self.pickup_point

    def get_destination(self):
        return self.destination

    def get_time(self):
        return self.time

    def get_done(self):
        return self.done

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
