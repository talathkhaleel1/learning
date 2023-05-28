from application_development.test.managing_courses_and_students.students import Student

class Course:

    def __init__(self, name_of_the_course, max_limit_of_participants):
        self.name_of_the_course = name_of_the_course
        self.max_limit = max_limit_of_participants

    def add(self, student_name):
        return student_name

    def remove(self, student_name):
        return student_name



