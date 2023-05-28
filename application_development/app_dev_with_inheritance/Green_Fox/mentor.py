# Create a Mentor class that has the same fields and methods as the Person class, and has the following additional
#
# fields:
# level: the level of the mentor (junior / intermediate / senior)
# methods:
# get_goal(): prints out "Educate brilliant junior software developers."
# introduce(): "Hi, I'm name, a age year old gender level mentor."
# The Mentor class has the following constructors:
#
# Mentor(name, age, gender, level)
# Mentor(): sets name to Jane Doe, age to 30, gender to female, level to intermediate

from inheritance.Green_Fox.person import Person

class Mentor(Person):

    def __init__(self, name, age, gender, level:str):
        super().__init__(name, age, gender)
        self.level = level


    def get_goal(self):
        print("Educate brilliant junior software developers.")

    def introduce(self):
        super().introduce()
        print(self.level)



