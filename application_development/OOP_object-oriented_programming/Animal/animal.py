# Create an Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one

class Animal:

    def __init__(self):
        self.hunger_value :int = 50 # __ it signifies to be  a private field. This can be used to make functions private \
        self.thirst_value: int = 50 # __ is used and will not get reflected in the main file. Private fields cannot be edited
                             # without altering the logic
                                              # getters and setters are used only for private fields and functions. \
                                              # If we have setters we can have new logic and develop on it, else it is diffcult \
                                              # to develop on the individual logic.

    def __str__(self):
        return "hunger:" + str(self.hunger_value) + "thirst: "+ str(self.thirst_value)

    def eat(self):
        self.hunger_value -= 1


    def drink(self):
        self.thirst_value -= 1


    def play(self):
        self.hunger_value += 1
        self.thirst_value += 1

