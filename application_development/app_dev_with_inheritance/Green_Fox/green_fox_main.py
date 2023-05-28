from inheritance.Green_Fox.person import Person
from inheritance.Green_Fox.student import Student
from inheritance.Green_Fox.mentor import Mentor
from inheritance.Green_Fox.sponsor import Sponsor
from inheritance.Green_Fox.cohort import Cohort


person1 = Person("Mark", 46, "male.")
person1.introduce()
person1.get_goal()


student1 = Student("Jane Doe", 30, "female.","The School of Life",0)
student1.introduce()
student1.get_goal()

mentor1 = Mentor('Gandhi', 148, 'male', 'senior mentor')
mentor1.introduce()# not printing beyond parent class details
mentor1.get_goal()

mentor2 = Mentor("Jane Doe", 30, "female.", 'intermediate mentor')
mentor2.introduce()
mentor2.get_goal()

sponsor1 = Sponsor("Jane Doe", 30, "female.", 'Google', 3)
sponsor1.introduce()
sponsor1.get_goal()

sponsor2 = Sponsor('Elon Musk', 46, 'male', 'SpaceX', 5)
sponsor2.introduce()
sponsor2.get_goal()

Awesome = Cohort("Awesome","students","mentors")
Awesome.add_student("John")
Awesome.add_student("Jane")
Awesome.add_mentor("Gandhi")
Awesome.add_mentor("Elon")
Awesome.info()
