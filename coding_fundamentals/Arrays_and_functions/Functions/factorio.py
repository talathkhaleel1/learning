# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(number):
    factorial = 1
    for i in range(1, number+1):# +1 as the input is taken to the value - 1 level only.
        factorial = factorial * i
    return factorial

print(factorio(10))
