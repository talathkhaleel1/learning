# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

number_saved = int(input("Please enter the number you want to save: "))
user_guess_number = int(input("Please enter the number you guessed: "))
result = ""
if user_guess_number < number_saved:
    result = "The stored number is higher."
elif user_guess_number > number_saved:
    result = "The stored number is lower."
elif user_guess_number == number_saved:
    result = "You found the number: 8"
print(result)
