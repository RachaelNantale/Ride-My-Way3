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


class User:
    """
    Class to represent the User model
    """

    def __init__(self, name, email, password, phone):
        self.id = uuid.uuid4().int
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone': self.phone

        }
