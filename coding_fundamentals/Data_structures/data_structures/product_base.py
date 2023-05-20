# We are going to represent our products in a map where the keys are strings representing \
# the product's name and the values are numbers representing the product's price.
#
# Create a map with the following key-value pairs.
#
# Product name (key)	Price (value)
# Eggs	200
# Milk	200
# Fish	400
# Apples	150
# Bread	50
# Chicken	550
# Create an application which solves the following problems.
#
# How much is the fish?
# What is the most expensive product?
# What is the average price?
# How many products' price is below 300?
# Is there anything we can buy for exactly 125?
# What is the cheapest product?

products = {"Eggs":200, "Milk":200, "Fish":400, "Apples":150, "Bread": 50, "Chicken":550}

# How much is the fish?
print("The price of fish is:",products["Fish"])

# What is the most expensive product?
print("most_expensive_product is", max(products, key=products.get))# to get the key whose value is greatest in the dictionary.

# What is the average price?
sum_of_prices = 0
for v in products.values():# we are taking only values for calculation
    sum_of_prices += v # the sum_of_prices is increased at every iteration by the value of v
    average_price = sum_of_prices / len(products)
print("average price is:", average_price)

# How many products' price is below 300?
for k,v in products.items(): # Sir this is executing but has some problem
    if v < 300: #as i am getting the count multiple time
        print(len(k))

# Is there anything we can buy for exactly 125?
print(125 in products)

# What is the cheapest product?
print(min(products, key=products.get)) #gives min valued key