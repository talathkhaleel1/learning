# Write a function that receives a string as an input and returns the most frequent \
# letter from the given string. Your solution should be case insensitive, \
# so a capital letter (like A) and its non-capital version (a) should be counted as \
# the same letter.
# In the given string there can be spaces as well, but your solution shouldn’t count spaces. \
# If there are multiple letters with the same occurrence, you can decide which one to return.
#
#
# print(most_common_letter('apple')) # should print p
# print(most_common_letter('This is not so hard')) # should print s

def most_frequent_letter(text):
    text_without_space = text.replace(" ", "")
    letter_counts = {}
    lower_text = text_without_space.lower()
    for letter in lower_text:
        if letter in letter_counts:
            continue
        letter_counts[letter] = lower_text.count(letter)
        key_with_highest_value = max(letter_counts, key=letter_counts.get)
    return key_with_highest_value

print(most_frequent_letter("apple"))
print(most_frequent_letter("This is not so hard"))

# Reference : https://www.entechin.com/how-to-find-the-max-value-in-a-dictionary-in-python/
# Reference : https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/

