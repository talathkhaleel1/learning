from abc import ABC, abstractmethod

class Aircraft(ABC):
    def __init__(self, max_ammo:int, base_damage:int):
        self.__max_ammo = max_ammo
        self.__base_damage = base_damage
        self.__ammo = 0

    def fight(self):
        damage = self.calculate_damage()
        self.__ammo = 0
        return damage

    def refill(self, available_ammo: int):
        if available_ammo <= 0:
            return 0

        if self.__ammo < self.__max_ammo:
            required = self.__max_ammo - self.__ammo

            if required < available_ammo:
                self.__ammo = self.__max_ammo
                return available_ammo - required
            else:
                self.__ammo += available_ammo
                return 0
        else:
            return available_ammo



    def get_status(self):
        return "Type " + self.getType() + ", Ammo: " + str(self.__ammo) +  ", Base Damage: " \
            + str(self.__base_damage) + ", All Damage: " + str(self.calculate_damage())

    def calculate_damage(self):
        return self.__base_damage * self.__ammo

    @abstractmethod
    def getType(self):
        pass