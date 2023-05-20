# Create an empty map where the keys are integers and the values are characters
#
# Print out whether the map is empty or not
#
# Add the following key-value pairs to the map
#
# Key	Value
# 97	a
# 98	b
# 99	c
# 65	A
# 66	B
# 67	C
# Print all the keys
#
# Print all the values
#
# Add value D with the key 68
#
# Print how many key-value pairs are in the map
#
# Print the value that is associated with key 99
#
# Remove the key-value pair where with key 97
#
# Print whether there is an associated value with key 100 or not
#
# Remove all the key-value pairs

map ={97:"a", 98:"b", 99:"c", 65:"A", 66:"B", 67:"C"}
print(map.keys()) # prints all the keys
print(map.values()) # prints all the values
map.update({68:"D"}) # adds new key_value_pair (also called items) to the existing dictionary
print(len(map)) # prints number_of_key_value_pairs(also called items) in the dictionary
print("The value for 99 is", map[99]) # prints the value of the given key, if avaialable
del map[97] #deletes the key_value_pair of the given key
print(map)
print(100 in map) #helps to know if such a key_value_pair is avaialable in the dictionary, returns a boolean value
map.clear() # clears the dictionary and makes it empty
print(map)