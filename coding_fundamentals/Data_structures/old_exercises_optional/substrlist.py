#  Create a function that takes a string and a list of string as a parameter
#  Returns the index of the string in the list where the first string is part of
#  Only need to find the first occurence and return the index of that
#  Returns `-1` if the string is not part any of the strings in the list

#  Example
# print(substrlist("ching", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `4`
# print(substrlist("not", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `-1`

def substrlist(string_to_find, list_of_words):
    for word in list_of_words:
        if string_to_find in word:
            return list_of_words.index(word)

    return  "-1"

print("Index of string to find in list 1:", substrlist("ching", ["this", "is", "what", "I'm", "searching", "in"]))
print("Index of string to find in list 2:", substrlist("not", ["this", "is", "what", "I'm", "searching", "in"]))

#reference
#https://www.w3schools.com/python/python_lists_comprehension.asp