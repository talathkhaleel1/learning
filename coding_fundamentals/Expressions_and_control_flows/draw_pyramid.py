# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

lines_in_pyramid = int(input("Please key in the number of lines: "))
for i in range(1, lines_in_pyramid+1, 2):# 2 is written to increase the number of the stars.
    print(" " * lines_in_pyramid+i * "*" )
    lines_in_pyramid = lines_in_pyramid - 1