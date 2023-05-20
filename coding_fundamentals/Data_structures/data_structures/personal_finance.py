# We are going to represent our expenses in a list containing integers.
#
# Create a list with the following items.
# 500, 1000, 1250, 175, 800 and 120
# Create an application which solves the following problems.
# How much did we spend?
# Which was our greatest expense?
# Which was our cheapest spending?
# What was the average amount of our spendings?

list = [500, 1000, 1250, 175, 800, 120]

# How much did we spend?
total_expenditure = sum(list)
print(total_expenditure)

# Which was our greatest expense?
greatest_expense = max(list)
print(greatest_expense)

# Which was our cheapest spending?
cheapest_expenditure = min(list)
print(cheapest_expenditure)

# What was the average amount of our spendings?
average_expenditure = total_expenditure/len(list)
print(average_expenditure)

