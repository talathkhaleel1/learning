class Plant:
    def __init__(self, type, color, minimum_water_amount, water_absorption):
        self.type = type
        self.color = color
        self.current_water_amount = 0
        self.minimum_water_amount = minimum_water_amount
        self. water_absorption = water_absorption

    def water(self, amount):
        absorbed_amount = amount * self.water_absorption # the amount of water a plant will get
        self.current_water_amount += absorbed_amount

    def __str__(self):
        watering_condition = "needs water" if self.current_water_amount < self.minimum_water_amount else "doesnt need water"
        return "The "+ self.color + " " + self.type + " " + watering_condition

