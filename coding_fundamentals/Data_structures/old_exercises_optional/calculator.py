# Create a simple calculator application which does read the parameters from the prompt
# and prints the result to the prompt.

# It should support the following operations, create a function called calculate():
# +, -, *, /, % and it should support two operands.

# The format of the expressions must be: {operation} {operand} {operand}.
# Examples: "+ 3 3" (the result will be 6) or "* 4 4" (the result will be 16)

# You should use the input() function to accept user input
# It should work like this:

# Start the program
# It prints: "Please type in the expression:"
# Waits for the user input
# Print the result
# Exit

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num1 > num2:
        return num1 / num2
    else:
        return num2 / num1

def remainder(num1, num2):
    if num1 > num2:
        return num1 % num2
    else:
        return num2 % num1

def arithmetic_opererations():
    arithmetic_opererations = ["+", "-", "*", "/", "%"]
    for i in arithmetic_opererations:
        if i == "+":
            return add()
        elif i == "-":
            return sub()
        elif i == "*":
            return multiply()
        elif i == "/":
            return divide()
        elif i == "%":
            return remainder()



def calculate(user_input):
    input = user_input.split(" ")
    operator = input[0]
    first_number = int(input[1])
    second_number = int(input[2])
    if operator == "+":
        return add(first_number, second_number)
    elif operator == "-":
        return sub(first_number, second_number)
    elif operator == "*":
        return multiply(first_number, second_number)
    elif operator == "/":
        return divide(first_number, second_number)
    elif operator == "%":
        return remainder(first_number, second_number)
    else:
        return "Invalid input"

user_input = input("Please type in the expression, eg: * 2 2: ")
print(calculate(user_input))