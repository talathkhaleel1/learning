# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was

lines_in_diamond = int(input("Please key in the number of lines: "))


for i in range(lines_in_diamond-1):
    print((lines_in_diamond-i) * ' ' + (2*i+1) * '*')# upper half of the diamond
for i in range(lines_in_diamond -1, -1, -1):# to reduce the number of stars for each line
    print((lines_in_diamond-i) * ' ' + (2*i+1) * '*')# second half of the diamond


#Logic used:

# range of -1 : this is used to give the shape of the diamonder
# print((lines_in_diamond-i) * ' ' + (2*i+1) * '*') - printing range * blank spaces* \
# (2*i+1) - two times the triangle drawing * the star pattern
# range(lines_in_diamond -1, -1, -1), the last -1 is to reduce the number of stars \

