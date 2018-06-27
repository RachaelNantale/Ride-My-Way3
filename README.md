[![Build Status](https://travis-ci.org/RachaelNantale/Ride-My-Way2.svg?branch=158657250-start-challenge-3)](https://travis-ci.org/RachaelNantale/Ride-My-Way2)
[![Coverage Status](https://coveralls.io/repos/github/RachaelNantale/Ride-My-Way2/badge.svg?branch=ch-testing-apiroutes)](https://coveralls.io/github/RachaelNantale/Ride-My-Way2?branch=ch-testing-apiroutes)

# Ride-My-Way2
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers  and passengers to join available ride offers. 

## Requirements
> pip install -r requirements.txt

## The API Endpoints

| End Point  | Description |
| ------------- | ------------- |
| GET /api/v1/rides | Fetch all the rideoffer |
| GET /api/v1/rides/<string:id>/ |  Fetch a single ride offer |
| POST /api/v1/rides |Create a ride offer |
| PUT /api/v1/rides/<string:id> |Modify a ride offer |
| DELETE /api/v1/rides/<string:id>   | Delete a ride offer|


