# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

from application_development.OOP.Petrol_Station.station import Station
from application_development.OOP.Petrol_Station.car import Car


car1 = Car(0, 210)
station1 = Station(200)
station1.refill(car1)
print(station1)