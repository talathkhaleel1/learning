# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)

def print_params(*arguments):# * means multiple arguments can be given
    phrase = ""
    for word in arguments:
        phrase += word
    print(phrase)

print_params("hello, ", "how are you?")

print_params("Bonjour Madame! ", "Vous allez bien?")

print_params("As Salaam Alaykum, ", "Kaifik?")

# reference
# https://www.geeksforgeeks.org/how-to-pass-multiple-arguments-to-function/

