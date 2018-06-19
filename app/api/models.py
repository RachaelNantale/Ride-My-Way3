import uuid
import json


class RideOffers:
    """
    class for ride offers
    """
    def __init__(self, driver,pickup_point,destination,time):
        self.id = uuid.uuid4().hex
        self.driver = driver
        self.pickup_point = pickup_point
        self.destination = destination
        self.time = time

    def json(self):
        """
        json representation of the Order model
        """
        return json.dumps({
            'id': self.id,
            'driver':self.driver,
            'pickup_point':self.pickup_point,
            'destination':self.destination,
            'time':self.time 
            })


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
        return json.dumps({
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'phone':self.phone
            
        })




