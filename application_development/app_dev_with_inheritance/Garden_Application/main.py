from inheritance.Garden_Application.garden import Garden
from inheritance.Garden_Application.flowers import Flower
from inheritance.Garden_Application.trees import Tree
from inheritance.Garden_Application.plant import Plant

garden = Garden()

garden.plants.append(Flower("yellow"))
garden.plants.append(Flower("blue"))
garden.plants.append(Tree("purple"))
garden.plants.append(Tree("orange"))

garden.water(40)
garden.water(70)