from app.api.models import RideOffers


class ValidateRideData:
    """ class to validate the ride offers """

    def validate_ride_offer(self, driver, pickup_point, destination, time):
        """ Function to validdate data entered while creating a request """
        if driver == "":
            return {"message": "Please Fill in driver details"}
        if pickup_point == "":
            return {"message": "Please Fill in the Pickup Point"}
        if destination == "":
            return {"message": "Please Fill in the Destination"}
        if time == "":
            return {"message": "Please Fill in the Time"}

    def validate_no_symbols(self, driver, pickup_point, destination, time):
        if driver.isalnum()is False or driver.strip(" ") == "  ":
            return {"message": "Please Fill in valid input"}
        if pickup_point.isalnum()is False or pickup_point.strip(" ") == "":
            return {"message": "Please Fill in valid input"}
        if destination.isalnum()is False or destination.strip(" ") == "":
            return {"message": "Please Fill in valid input"}
        if time.isalnum()is False or time.strip(" ") == "":
            return {"message": "Please Fill in valid input"}
