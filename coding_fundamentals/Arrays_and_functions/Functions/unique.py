#  Create a function that takes a list of numbers as a parameter
#  Returns a list of numbers where every number in the list occurs only once

# def unique(arr):
#     pass

#  Example
# print(unique([1, 11, 34, 11, 52, 61, 1, 34]))
#  should print: `[1, 11, 34, 52, 61]`

# return all items in the list without duplication
def unique(arr):
    unique_list = list(set(arr))
    return unique_list

# reference for the above solution
# https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

# return the items that are present only once in the input list

# def unique(list):
#     unique_list = []
#     for i in list:
#         if list.count(i) == 1:
#             unique_list.append(i)
#     return unique_list #  to get the desired result return or print should be at the same indent as \
    # the condition or iteration you need to fulfill

print(unique([1, 11, 34, 11, 52, 61, 1, 34]))

