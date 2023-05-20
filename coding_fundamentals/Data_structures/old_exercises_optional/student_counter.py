students = [
        {'name': 'Theodor', 'age': 3, 'candies': 2},
        {'name': 'Paul', 'age': 9.5, 'candies': 2},
        {'name': 'Mark', 'age': 12, 'candies': 5},
        {'name': 'Peter', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'George', 'age': 10, 'candies': 1}
]

# create a function that takes a list of students and prints:
# - how many candies are owned by students altogether

# create a function that takes a list of students and prints:
# - The sum of the age of people who have less than 5 candies


def total_of_candies(list):
    total_candies = 0
    for i in range(len(list)): # first unpack dictionary from list
        student_dict = list[i]
        total_candies += student_dict["candies"]
    return total_candies # write return function here as we need to iterate through
    # each element of the list

print("total_candies:",  total_of_candies(students))


def sum_of_age(list):
    total_age = 0
    for i in range(len(list)):
        student_dict = list[i]
        if student_dict["candies"] < 5: # first pull out data for students who have less than 5 candies
                total_age += student_dict["age"] # then for those students,\
                # increase the total age by the values of the key named "age"
    return total_age

print("Sum of the age of students who have less than five candies:", sum_of_age(students))

#reference
# https://docs.google.com/spreadsheets/d/1HihkKPmceNyOeXIgce07gyrr5s1hqojlWq2X_JSVPLE/edit#gid=0

