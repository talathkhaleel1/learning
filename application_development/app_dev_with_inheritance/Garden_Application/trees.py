# two trees (purple and orange)
from inheritance.Garden_Application.plant import Plant

class Tree(Plant):
    def __init__(self, color):
        super().__init__("tree", color, 10, 0.4)


