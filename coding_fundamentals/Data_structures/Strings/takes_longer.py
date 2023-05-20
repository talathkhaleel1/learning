# When saving this quote a disk error has occured. Please fix it.
# Add "always takes longer than" between the words "It" and "you"

quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
word_to_add_after = quote.find("you")# always gives till the value before the specified one
quote = quote[:word_to_add_after] + "always takes longer than " + quote[word_to_add_after:]
print(quote)