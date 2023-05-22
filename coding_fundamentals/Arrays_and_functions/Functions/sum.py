# Write a function called `sum` that returns the sum of numbers from zero to the given parameter



def sum(num_limit):
    result = 0
    for i in range(0, num_limit):
        i += 1
        result = result + i
    return result



print(sum(10))
