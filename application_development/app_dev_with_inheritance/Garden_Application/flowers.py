# two flowers (yellow and blue)
from inheritance.Garden_Application.plant import Plant


class Flower(Plant):
    def __init__(self, color):
        super().__init__("flower", color, 5, 0.75)


