# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was

# Sir I found this on internet and I have just made notes as per my understanding

m = 10 # sides of the square
for i in range(m): # for loop for two parallel sides of square
    for j in range(m): # # for loop for other two parallel sides of square
        print('%' if i in [0, m-1] or j in [0, m-1] else ' ', end='')
    print()


# '%' --> the symbol used to draw the shape.
# i in [0, n-1] --> means if the iteration index - i is at the range of 0 , side n-1
# j in [0, m-1] --> means if the iteration index - j is at the range of 0 , side m-1
# else ' ' --> means blanks to be added for all other iterations other than those specified above\
#              to get this shape of the square.
# end ='' --> means after one iteration move to the next line for the second iteration.

side_of_the_square = int(input("Please specify the size of the required square: "))
for i in range(side_of_the_square): # --> one set of parallel sides of the square
    for j in range(side_of_the_square): # --> the other set of parallel sides of the square
        print("%" if i in [0,side_of_the_square-1] or j in [0, side_of_the_square-1] else " ", end='')
    print()