from application_development.test.managing_courses_and_students.courses import Course
from application_development.test.managing_courses_and_students.students import Student

itlb = Course('ITLB', 3)
jane = Student('Jane')
john = Student('John')
kate = Student('Kate')
kyle = Student('Kyle')
itlb.add(jane)
itlb.add(john)
itlb.add(kate)
print(itlb) # should print: ITLB course has 3 students
itlb.add(kyle) # should print: The course is full.
print(itlb) # should print: ITLB course has 3 students
itlb.remove('Jane')
print(itlb) # should print: ITLB course has 2 students
itlb.remove('Jane')
print(itlb) # should print: ITLB course has 2 students