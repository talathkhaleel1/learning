# Car
# gas_amount
# capacity

class Car:
    def __init__(self, gas_amount, capacity):
        self.gas_amount = gas_amount
        self.capacity = capacity

    def get_freespace(self):
        freespace = self.capacity - self.gas_amount
        return freespace

    def refill(self, amount):
        self.gas_amount += amount
