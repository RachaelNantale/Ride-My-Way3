[![Build Status](https://travis-ci.org/RachaelNantale/Ride-My-Way3.svg?branch=add-more-tests)](https://travis-ci.org/RachaelNantale/Ride-My-Way3)
[![Coverage Status](https://coveralls.io/repos/github/RachaelNantale/Ride-My-Way3/badge.svg?branch=add-more-tests)](https://coveralls.io/github/RachaelNantale/Ride-My-Way3?branch=add-more-tests)

# Ride-My-Way3
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers  and passengers to join available ride offers. 

## Requirements
> pip install -r requirements.txt

## Features
- Create user accounts that can signin/signout from the app. 
- Get all available ride offers.
- Get the details of a ride offer.
- Make a ride request (N.B: this is a response to a ride offer)
- Create ride offer.
- View all requests for a ride offer.
- Accept or reject a request for a ride offer.


## Prerequisites
- [PostgreSQL](https://www.postgresql.org/)
- [Python](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiYlbSpo4ncAhXCT8AKHXMeAf8QFggnMAA&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&usg=AOvVaw3VuYRIaaa-SL5nRa6pfny0)


## The API Endpoints

| End Point  | Description |
| ------------- | ------------- |
|POST /api/v1/auth/signup       | used for signing up a user     |
|POST /api/v1/auth/login        | used to login into the api | 
| GET /api/v1/rides | Fetch all the rideoffer |
| GET /api/v1/rides/<string:id>/ |  Fetch a single ride offer |
| POST /api/v1/rides |Create a ride offer |
| POST /api/v1/<string:id>/requests| Make a request
|GET /api/v1/users/rides/<string:id>/requests| Fetch all the requests that made to a given ride offer |
|PUT|  /api/v1/users/rides/<string:id>/requests/<string:request_id>| used to accept or reject a ride join request     |






