# Create a Student class that has the same fields and methods as the Person class, and has the following additional
#
# fields:
# previous_organization: the name of the student’s previous company / school
# skipped_days: the number of days skipped from the course
# methods:
# get_goal(): prints out "Be a junior software developer."
# introduce(): "Hi, I'm name, a age year old gender from previous_organization who skipped skipped_days days from the course already."
# skip_days(number_of_days): increases skipped_days by number_of_days
# The Student class has the following constructors:
#
# Student(name, age, gender, previous_organization): beside the given parameters, it sets skipped_days to 0
# Student(): sets name to Jane Doe, age to 30, gender to female, previous_organization to The School of Life, skipped_days to 0

from inheritance.Green_Fox.person import Person

class Student(Person):

    def __init__(self,  name: str, age: int, gender: str, previous_organization: str, skipped_days: int ):
        super().__init__(name, age,gender)# to inherit fields from parent class
        self.previous_organization = previous_organization #add only the other required fields apart from parent class fields
        self.skipped_days = skipped_days

    def get_goal(self):
        print("Be a junior software developer.")

    def introduce(self):
        super().introduce() # to use the introduce function from parent class
        print("from "+self.previous_organization+", who skipped "+str(self.skipped_days)+" days from the course already")

    def skip_days(self, number_of_days: int):
        self.number_of_days = number_of_days
        self.skipped_days += number_of_days