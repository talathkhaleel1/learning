from application_development.OOP import Counter

counter1 = Counter() #creating an instance
counter2 = Counter()

print(counter1)
print(counter2)

counter1.__add__(5)
print(counter1)
print(counter2)

counter2.__add__(10)
print(counter1)
print(counter2)

counter1.add()
print(counter1)
print(counter2)

counter2.add()
print(counter1)
print(counter2)

counter1.current_value()
print(counter1)
print(counter2)

counter2.current_value()
print(counter1)
print(counter2)

counter1.reset_value()
print(counter1)
print(counter2)

counter2.reset_value()
print(counter1)
print(counter2)