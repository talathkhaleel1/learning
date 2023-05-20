# Accidentally I messed up this quote from Richard Feynman.
# Two words are out of place
# Your task is to fix it by swapping the right words with code

# Also, print the sentence to the output with spaces in between.
# Create a function called quote_swap()

# words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]
# print(quote_swap(words))
# Expected output: "What I cannot create I do not understand."

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

def quote_swap(quote):
    replace_do = quote.index("do")
    replace_cannot = quote.index("cannot")
    quote[replace_do], quote[replace_cannot] = quote[replace_cannot],quote[replace_do]
    new_quote = ""
    for i in quote:
        new_quote = " ".join(quote)
    return new_quote

print(quote_swap(words))
