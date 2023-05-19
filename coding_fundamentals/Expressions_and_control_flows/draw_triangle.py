# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

lines_in_triangle = int(input("Please key in the number of lines: "))
for i in range(1, lines_in_triangle+1): #increament of one star in each line
    print("*" * i)