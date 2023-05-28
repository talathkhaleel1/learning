# Create Student and Teacher classes
# Student
# learn() -> prints the student is learning something new
# question(teacher) -> calls the teachers answer method
# Teacher
# teach(student) -> calls the students learn method
# answer() -> prints the teacher is answering a question
# Instantiate a Student and Teacher object
# Call the student's question() method and the teacher's teach() method

from application_development.OOP import Student, Teacher


student1=Student() # student instance
teacher1=Teacher() # teacher instance

student1.question(teacher1)
teacher1.teach(student1)

