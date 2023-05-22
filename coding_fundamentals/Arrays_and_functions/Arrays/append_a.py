# - Create a variable named `animals`
#   with the following content: `["koal", "pand", "zebr"]`
# - Add all elements an `"a"` at the end

animals = ["koal", "pand", "zebr"]
for i in range(len(animals)):
    animals[i] = animals[i] + "a"
print(animals)

# NOTE:
#to modify each element of the list use range and len for iteration and modify by index. \
# This will modify the content of the list.