# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

count_limit = 101
for i in range(count_limit):
    result = ""
    if i % 3 == 0:
        result = "Fizz"
    elif i % 5 == 0:
        result = "Buzz"
    elif i % 15 == 0:
        result = "FizzBuzz"
    print(i, ":", result)
