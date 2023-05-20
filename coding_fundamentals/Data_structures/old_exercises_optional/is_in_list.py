# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

# list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
#
# print(check_nums(list_of_numbers))

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]


def check_nums(list):

    for i in range(len(list)):
        if i % 4 == 0:
            return True
        else:
            return False

print(check_nums(list_of_numbers))





