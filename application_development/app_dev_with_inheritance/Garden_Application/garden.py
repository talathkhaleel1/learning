from inheritance.Garden_Application.flowers import Flower
from inheritance.Garden_Application.trees import Tree
from inheritance.Garden_Application.plant import Plant
class Garden:

    def __init__(self):
        self.plants = []

    def show_garden(self):
        for plant in self.plants:
            print(self.plant)



    def water(self, amount):
        print("Watering with "+ str(amount))
        water_per_plant = amount / (len(self.plants)
        for plant in self.plants:
            plant.water(water_per_plant)


    