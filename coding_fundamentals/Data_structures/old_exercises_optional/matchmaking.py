# Write function that joins the two lists by matching one girl with one boy in a new list
# If someone has no pair, he/she should be the element of the list too
# Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

# girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
# boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]
#
# print(making_matches(girls, boys))

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]

def making_matches(list1, list2):
    pairs = []                                      # to pair up we use range and maximum
    for i in range(max(len(list1), len(list2))): # range is used as we need to include all elements\
                                                # to the extent maximum of both lists as we do not know\
                                                # the length of any list.
        if i < len(list1): # add unpaired elements of the list
            pairs.append(list1[i])
        if i < len(list2):# add unpaired elements of the list
            pairs.append(list2[i])
    return pairs

print(making_matches(girls, boys))


