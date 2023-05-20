a_list = ["a", "b", "c", "d"]

# range() creates a sequence of numbers that you can use in iteration
# Index will be a number starting from 0 till the end of the list:
for index in range(len(a_list)):
    # Then you can use indexes to refer to elements:
    print(a_list[index])

# You can go through the list without the range() function
for item in a_list:
    # Then item will be directly the content of the list, you can reach them without indexes
    print(item)

print("Try to print every second item")
# What happens when you need to print every second item?
# You need indexes for that:
for index in range(len(a_list)):
    if index%2 == 0:
        print(a_list[index])

# So, the general rule is to use range() when you want to use indexes inside iteration

# Another case is when you want to modify an item:
for item in a_list:
    if item == "a":
        item = "aa"

# The list is not modified:
print(a_list)

# But you can modify items by referring to the items with indexes:
for index in range(len(a_list)):
    if a_list[index] == "a":
        a_list[index] = "aa"

# The list is now is modified:
print(a_list)

# range and len are always used together?

# Not necessarily
# They are independent functions
# you can say: for index in range(9):

#reference
# https://pynative.com/python-range-function/

# yet, when you want to go through items of a list, \
# then you need a sequence of numbers that goes till the length of the list
# shortly: you need a range that is just as long as the list you want to go through
# this is why we often use len() for range()