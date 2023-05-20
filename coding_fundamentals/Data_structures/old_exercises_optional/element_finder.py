# Write a function that checks if the list contains "7" \
# if it contains return "Hoorray" otherwise return "Noooooo"

# numbers = [1, 2, 3, 4, 5, 6, 8];
# print(contains_seven(numbers))
# The output should be: "Noooooo"
# Do this again with a different solution using different list functions!

numbers = [1, 2, 3, 4, 5, 6, 8]
specify_number = 7
def contains_seven(list):
    for i in list:
        if i == specify_number:
            return "Hoorray"
        else:
            return "Noooooo"

print(contains_seven(numbers))