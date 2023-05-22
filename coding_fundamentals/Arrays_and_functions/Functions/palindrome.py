# Create a function named create palindrome following your current language's style guide. \
#  What is a palindrome?
# a word, phrase, or sequence that reads the same backwards as forwards

# It should take a string, create a palindrome from it and then return it.
#
# Examples
# input	output
# ""	""
# "greenfox"	"greenfoxxofneerg"
# "123"	"123321"

word = "racecar"
def create_palindrome(word):
    word_reverse = word[::-1]
    return word + " " + word_reverse

print(create_palindrome(word))