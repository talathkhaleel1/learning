from Aircraft import Aircraft

class F16(Aircraft):
    def __init__(self):
        super().__init__(8, 30)

    def getType(self):
        return "F16"

    def isPriority(self):
        return False