from Aircraft import Aircraft

class F35(Aircraft):
    def __init__(self):
        super().__init__(12, 50)

    def getType(self):
        return "F35"

    def isPriority(self):
        return True