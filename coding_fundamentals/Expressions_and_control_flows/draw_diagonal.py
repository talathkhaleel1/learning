# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %%  %
# % % %
# %  %%
# %   %
# %%%%%
#
# The square should have as many lines as the number was


#Logic used:
# Note: always start with the analysis of features of a given polygon

# m, n = 10, 10 # parallell sides of the square. Since all sides of the square are equal
#we can take one variable
# size_of_diagonal = 5 because a diagonal divides a square into two equal triangles. Thus we divide the
# side_of the_square by 2 to get side_of_the_diagonal.



side_of_the_square = 10
for i in range(side_of_the_square):# for loop for side m
    for j in range(side_of_the_square):# for loop for the other parallel side m
        if(i == 0 or i == side_of_the_square - 1 or j == 0 or j == side_of_the_square - 1
           or i == j):
            print('* ', end = '')# to print stars in the stars specified in the position of the if statements
        else:
            print('  ', end = '')# to leave blank spaces in all other positions
    print()

    # i == 0 or i == m -1 --> prints parallel sides of the square
    # j == 0 or j == m - 1 --> prints the other parallel sides of the square
    # or i == j or j == (m - 1) --> prints the diagonal and \
    # so m-1 to avoid overlapping at the lower right edge of diagram