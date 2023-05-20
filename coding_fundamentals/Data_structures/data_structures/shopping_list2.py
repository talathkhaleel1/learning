# Represent the following products with their prices
#
# Product	Amount
# Milk	1.07
# Rice	1.59
# Eggs	3.14
# Cheese	12.60
# Chicken Breasts	9.40
# Apples	2.31
# Tomato	2.58
# Potato	1.75
# Onion	1.10
# Represent Bob's shopping list
#
# Product	Amount
# Milk	3
# Rice	2
# Eggs	2
# Cheese	1
# Chicken Breasts	4
# Apples	1
# Tomato	2
# Potato	1
# Represent Alice's shopping list
#
# Product	Amount
# Rice	1
# Eggs	5
# Chicken Breasts	2
# Apples	1
# Tomato	10
# Create an application which solves the following problems.
#
# How much does Bob pay?
# How much does Alice pay?
# Who buys more Rice?
# Who buys more Potato?
# Who buys more different products?
# Who buys more products? (piece)

shopping_list = {"Milk":1.07, "Rice":1.59, "Eggs":3.14, "Cheese":12.60, "Chicken Breasts":4, \
                 "Apples":2.31, "Tomato":2.58, "Potato":1.75, "Onion":1.10}

Bobs_shopping_list = {"Milk":3, "Rice":2, "Eggs":2, "Cheese":1, "Chicken Breasts":4, "Apples":1,\
                      "Tomato":2, "Potato":1}

Alices_shopping_list = {"Rice":1, "Eggs":5, "Chicken Breasts":2, "Apples":1, "Tomato":10}


def total_expenditure(list_name):
    total_payment = 0
    for v in list_name.values():
        total_payment += v
    return("Total payment:", total_payment)


print(total_expenditure(Bobs_shopping_list)) # How much does Bob pay? # The value here is not printing
print(total_expenditure(Alices_shopping_list)) # How much does Alice pay? # The value here is not printing

# Who buys more Rice?
# Who buys more Potato?


def buys_more(product_name, list_name1, list_name2):
    if list_name1[product_name] > list_name2[product_name]:
        return ("Bob bought more rice.")
    else:
        return ("Alice bought more rice.")
#
print(buys_more("Rice", Bobs_shopping_list, Alices_shopping_list))
# print(buys_more("Potato", Bobs_shopping_list, Alices_shopping_list))# Shows an error as Potato \
# not in Alice's shopping list.



# Who buys more different products?
if len(Bobs_shopping_list) > len(Alices_shopping_list):
    print("Bob has bought more different products.")
else:
    print("Alice has bought more different products.")

# Who buys more products? (piece)

Bob_values = Bobs_shopping_list.values()
Bobs_total_values = sum(Bob_values)

Alice_values = Alices_shopping_list.values()
Alices_total_values = sum(Alice_values)

if Bobs_total_values > Alices_total_values:
    print("Bob bought more stuff.")
else:
    print("Alice bought more stuff.")
#