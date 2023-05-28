# Create a Person class with the following fields:
#
# name: the name of the person
# age: the age of the person (whole number)
# gender: the gender of the person (male / female)
# And the following methods:
#
# introduce(): prints out "Hi, I'm name, a age year old gender."
# get_goal(): prints out "My goal is: Live for the moment!"
# And the following constructors:
#
# Person(name, age, gender)
# Person(): sets name to Jane Doe, age to 30, gender to female

class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender


    def introduce(self):
        print("Hi, I'm "+self.name+","+" "+ "a "+ str(self.age)+ " year old "+self.gender)

    def get_goal(self):
        print("My goal is: Live for the moment!")

