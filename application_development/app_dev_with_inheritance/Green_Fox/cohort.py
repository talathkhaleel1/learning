# Create a Cohort class that has the following
#
# fields:
# name: the name of the cohort
# students: a list of Students
# mentors: a list of Mentors
# methods:
# add_student(Student): adds the given Student to students list
# add_mentor(Mentor): adds the given Mentor to mentors list
# info(): prints out "The name cohort has len(students) students and len(mentors) mentors."
# The Cohort class has the following constructors:
#
# Cohort(name): beside the given parameter, it sets students and mentors as empty lists


class Cohort:

    def __init__(self, name: str, students: [], mentors: []):
        self.name = name
        self.students = students
        self.mentors = mentors

    def add_student(self, student):
         pass

    def add_mentor(self, mentor):
        pass

    def info(self):
        print("The "+self.name+" cohort has "+ str(len(self.students))+" students and " + str(len(self.mentors))+" mentors.")
