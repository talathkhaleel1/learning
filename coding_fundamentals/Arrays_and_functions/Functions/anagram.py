# Create a function named is anagram following your current language's style guide. \
#  What is an anagram?
# a word, phrase, or name formed by rearranging the letters of another

# It should take two strings and return a boolean value depending on whether its an anagram or not.


word1 = "race, part, heart"
word2 = "care, trap, earth"

def anagram(word1, word2):
    if len(word1) == len(word2):
        return sorted(word1) == sorted(word2)


print(anagram(word1, word2))