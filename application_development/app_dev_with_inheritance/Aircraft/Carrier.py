from Aircraft import Aircraft

class Carrier:
    def __init__(self, initial_ammo, health_point):
        self.__aircrafts = []
        self.__initial_ammo = initial_ammo
        self.__ammo = initial_ammo
        self.__health_point = health_point

    def add(self, aircraft: Aircraft):
        self.__aircrafts.append(aircraft)

# region - Not yet implemented:
# If there is not enough ammo then it should start to fill the aircrafts with priority first
# endregion

    # It should fill all the aircraft with ammo and
    # subtract the needed ammo from the ammo storage
    def fill(self):
        # If there is no ammo when this method is called, it should throw an exception
        if self.__ammo <= 0:
            raise Exception("Sorry, no ammo enough")

        for aircraft in self.__aircrafts:
            if self.__ammo <=0:
                break

            self.__ammo = aircraft.refill(self.__ammo)
