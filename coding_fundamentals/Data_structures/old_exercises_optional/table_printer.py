# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]



def print_ingredients(list):
	print("Ingredients", "Needs_cooling", "in_stock", )
	# first unpack dictionary from list
	for i in range(len(list)):
		grocery = list[i]
		if grocery["in_stock"] is 0:# to replace value, 0 to "-"
			grocery["in_stock"] = "-"
			# two independent checks
		if grocery["needs_cooling"] == True: #to replace value, True to "Yes"
			grocery["needs_cooling"] = "Yes"
		elif grocery["needs_cooling"] == False: # #to replace value, False to "No"
			grocery["needs_cooling"] = "No"
		print(grocery["name"]," ", grocery["needs_cooling"]," ",grocery["in_stock"])

print_ingredients(ingredients)

# reference
# to change values in a dictionary, including boolean
# https://hmn.stackfinder.net/questions/66049789/replace-all-boolean-values-in-a-dict-by-a-corresponding-value-without-looping-th



# reference
# https://www.geeksforgeeks.org/python-program-to-print-the-dictionary-in-table-format/