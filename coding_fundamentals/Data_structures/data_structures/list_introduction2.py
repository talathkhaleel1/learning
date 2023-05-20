# Create a list ('List A') which contains the following values
# Apple, Avocado, Blueberries, Durian, Lychee
# Create a new list ('List B') with the values of List A
# Print out whether List A contains Durian or not
# Remove Durian from List B
# Add Kiwifruit to List A after the 4th element
# Compare the size of List A and List B
# Get the index of Avocado from List A
# Get the index of Durian from List B
# Add Passion Fruit and Pomelo to List B in a single statement
# Print out the 3rd element from List A

List_A = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
List_B = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]
print("Durian" in List_A)# to know if an element in a list. This returns a boolean value
# List_B.remove("Durian") #This execution is commented to get us the answer for the previous print statement,
# else the code with throw up an error
List_A.insert(4,"Kiwifruit")
print(List_A)
if len(List_A) == len(List_B)== True:
    print(True)
elif len(List_A) < len(List_B):
    print("Number of elements in List_A is less than List_B")
else:
    print("Number of elements in List_A is more than List_B")
print(List_A.index("Avocado"))
print(List_B.index("Durian"))
List_B += ("Passion Fruit", "Pomelo")
print(List_B)
print(List_A[2])