# - Create a variable named `orders`
#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders`

orders = ["first", "second", "third"]
first_element = orders[0]
third_element = orders[2]
orders[0],orders[2] = third_element,first_element
print(orders)
