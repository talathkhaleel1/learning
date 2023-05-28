# Student
# learn() -> prints the student is learning something new
# question(teacher) -> calls the teachers answer method


# from typing import TYPE_CHECKING # tried this but does not work.
# if TYPE_CHECKING:


class Student:

    def __init__(self):
        pass

    def learn(self):
        print("The student is learning something new.")


    def question(self, teacher):
        teacher.answer()

