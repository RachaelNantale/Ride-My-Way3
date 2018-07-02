import re
from app.api.models.ride import *
# from app.api.models.user import User


def validate_ride_input(driver, pickup_point, destination, time, errors):
    """ Function to validdate data entered while creating a request """
    result = True
    if driver is None or len(driver) > 20:
        errors.append(
            'Driver input must be provided and should be between 4 and 20 \
                characters long ')
        result = False

    if driver.alnum():
        errors.append('Please donot imput symbols')
        result = False

    if pickup_point is None or len(pickup_point) > 25:
        errors.append(
            'Pick up point input must be provided and should be between \
                4 and 20 characters long')
        result = False

    if pickup_point.alnum():
        result = False

    if destination is None or len(destination) > 20:
        errors.append(
            'Destination input must be provided and should be between 4 \
                and 20 characters long')
        result = False
    if destination.alnum():
        result = False

    if time is None or len(time) < 3 or len(time) > 10:
        errors.append(
            'Time input must be provided and should be between 3 and 10 \
                characters long and dont use symbols')
        result = False

    if time.alnum():
        result = False
    return result


def validate_user_input(self, username, email, password, phone, errors):
    result = True

    if re.compile('[!@#$%^&*:;?><.0-9]').match(username):
        errors.append('Invalid characters not allowed')
        result = False

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        errors.append('Enter valid email')
        result = False
    if len(password) < 5:
        errors.append('Password is too short')
        result = False

    if len(phone) < 10:
        errors.append('Phone number is too short')
        result = False
    return result

# ----------------------------------------------------------------------------------------------------------
