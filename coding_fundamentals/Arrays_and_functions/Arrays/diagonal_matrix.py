# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

list_size = 4 # to give dynamic value - generalising approach
matrix = []
for i in range(list_size): # range to reach out to every element of the list
    matrix.append([0] * list_size)# as we need 0s in the list
    matrix[i][i] = 1 # to change value from 0 to 1 in every iteration.
                    # \Here we add 1 at the same position of the iterating number
    print(matrix[i])# i is specified to imbibe the dynamic concept in execution of the programme