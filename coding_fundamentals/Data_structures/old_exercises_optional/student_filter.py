students = [
        {'name': 'Mark', 'age': 9.5, 'candies': 2},
        {'name': 'Sean', 'age': 10, 'candies': 1},
        {'name': 'Clark', 'age': 7, 'candies': 3},
        {'name': 'Paul', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average


# Who has got more candies

def got_more_than_4candies(list):
    student_names = []  # emplty list to be filled with names of students based on condition
    # first unpack the dictionary from list
    for i in range(len(list)):
        student_dictionary = list[i]
        if student_dictionary["candies"] > 4: # to extract data of students who have more than 4 candies
            student_names.append(student_dictionary["name"])
            return student_names

print("Students having more tahn four candies are:", got_more_than_4candies(students))


# finding average of candies

def average_candies(list):
    total_candies = 0
    # first unpack the dictionary from list
    for i in range(len(list)):
        student_dictionary = list[i]
        number_of_students = len(student_dictionary["name"])
        total_candies += student_dictionary["candies"]
        average_of_candies = total_candies / number_of_students
    return average_of_candies

print("Average number of candies:", average_candies(students))


