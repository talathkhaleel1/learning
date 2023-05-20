# We are going to represent a shopping list in a list containing strings.
#
# Create a list with the following items.
# Eggs, milk, fish, apples, bread and chicken
# Create an application which solves the following problems.
# Do we have milk on the list?
# Do we have bananas on the list?

shopping_list = ["Eggs", "milk", "fish", "apples", "bread", "chicken"]

# Do we have milk on the list?
if "milk" in shopping_list:
    print("milk in shopping list")
else:
    print("Sorry, no milk in shopping list")

# Do we have bananas on the list?
if "bananas" in shopping_list:
    print("bananas in shopping list")
else:
    print("Sorry, no bananas in shopping list")