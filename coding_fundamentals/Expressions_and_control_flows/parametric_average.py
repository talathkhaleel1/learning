# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4


# get a number from the input
# create a range that counts from 0  to this number
# in every loop, get an input from the user and add it to a sum variable
# finally calculate the sum and the average based on the initial number and \
# the value of the sum variable

list_of_values = []# empty list we need to fill with numbers
number = int(input("Please enter the number of elements you would like to have: "))# input to enter\
                                            # the number of elements one wants in the list_of_values
while len(list_of_values) < number : #use while loop and iterate through the list and \
                                    # append the list with the  input of number_to_enter
    number_to_enter = int(input("Please specify a number you want to add: "))
    list_of_values.append(number_to_enter)

n = len(list_of_values)
sum = sum (list_of_values)
print("Sum: ",sum)
average = sum / n
print("Average: ", average)
