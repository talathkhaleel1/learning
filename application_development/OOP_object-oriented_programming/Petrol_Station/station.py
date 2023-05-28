# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount

from application_development.OOP.Petrol_Station.car import Car

class Station:
    def __init__(self, gas_amount):
        self.gas_amount = gas_amount


    # def refill(self, car):
    #     self.gas_amount -= car.get_freespace()
    #     car.refill()

    def refill(self, car: Car):
        if self.gas_amount >= car.get_freespace():
            self.gas_amount -= car.get_freespace()
            car.refill(car.capacity)
        else:
            car.refill(self.gas_amount)
            self.gas_amount = 0



