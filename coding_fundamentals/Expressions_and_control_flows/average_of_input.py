# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
number_list = []
while len(number_list) < 5 : #use while loop and iterate through the list and append the list with the number
    number_to_add = int(input("Please specify a number you want to add: "))
    number_list.append(number_to_add)

# Logic used:

#     create an empty list
# create a loop that runs 5 times
# at every loop ask for a number and add it to the list
#
# then you have the numbers in that list and can calculate the sum and average


n = len(number_list)
sum = sum (number_list)
print("Sum: ",sum)
average = sum / n
print("Average: ", average)

