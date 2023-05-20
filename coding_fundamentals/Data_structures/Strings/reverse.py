# Create a function called 'reverse' which takes a string as a parameter
# The function reverses it and returns with the reversed string


toBeReversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"


def reverse(string):
    toBeReversed = string[::-1]
    return toBeReversed

print(reverse(toBeReversed))