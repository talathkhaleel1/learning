# We are going to play with lists. Feel free to use the built-in methods where possible.
#
# Create an empty list which will contain names (strings)
# Print out the number of elements in the list
# Add William to the list
# Print out whether the list is empty or not
# Add John to the list
# Add Amanda to the list
# Print out the number of elements in the list
# Print out the 3rd element
# Iterate through the list and print out each name
# William
# John
# Amanda
# Iterate through the list and print
# 1. William
# 2. John
# 3. Amanda
# Remove the 2nd element
# Iterate through the list in a reversed order and print out each name
# Amanda
# William
# Remove all elements

names = []
print(len(names))

names.append("William")
names += ("John", "Amanda")
print(names)
# this can also be written as names += ["John", "Amanda"] - this will add both the elements at the same time
print(len(names))
print(names[2])
for name in names:
    print(name)

for i in range(len(names)):
    print(i+1 ,". ", end="")
    print(names[i])

names.remove("John")
print(names)

names.reverse()
print(names)
names = []
print(names)


