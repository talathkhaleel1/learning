# Teacher
# teach(student) -> calls the students learn method
# answer() -> prints the teacher is answering a question


# from typing import TYPE_CHECKING
# if TYPE_CHECKING:
# from OOP.TeacherStudent.student import Student

class Teacher:

    def __init__(self):
        pass


    def teach(self, student: Student):
        student.learn()


    def answer(self):
        print("The teacher is answering a question")