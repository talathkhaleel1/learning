from trail_exam.businessman import BusinessMan
from trail_exam.shop import Shop
from trail_exam.grocery_shop import GroceryShop
from trail_exam.coffee_shop import CoffeeShop

tesco = GroceryShop('Tesco')
starbucks = CoffeeShop('StarBucks', 3)
johndoe = BusinessMan('John Doe')
johndoe.add(tesco) # should print: John Doe has a new business: Tesco
johndoe.add(starbucks) # should print: John Doe has a new business: StarBucks
print(johndoe) # should print: John Doe has 2 businesses: Tesco, StarBucks
# tesco.add('milk', 100) # since there's no price for milk in Tesco yet, it should print: milk can't be added to Tesco without a price
# tesco.add('milk', 10, 2) # should print: milk amount in Tesco: 10, price: 2$
# tesco.add('milk', 5, 1) # the given price is less than the current, so the price doesn't change: milk amount in Tesco: 15, price: 2$
# tesco.add('potato', 1, 1) # should print: potato amount in Tesco: 1, price: 1$
# tesco.sell('beer') # should print: There's no beer in Tesco
# tesco.sell('butter') # should print: There's no butter in Tesco
# tesco.sell('potato', 5) # should print: Tesco doesn't have enough potato, only 1 available
# tesco.sell('potato') # should print: Tesco sold potato (1) for 1$
# tesco.sell('potato') # should print: There's no potato in Tesco
# tesco.sell('milk', 3) # should print: Tesco sold milk (3) for 6$
# tesco.sell('milk', 2, True) # selling with bag, should print: Tesco sold milk (2) for 5$
# tesco.add('milk', 5, 2.5) # the given price is more than the current, so it prints: milk amount in Tesco: 15, price: 2.5$
# tesco.sell('milk', 16) # should print: Tesco doesn't have enough carrot, only 15 available
# starbucks.add('milk', 10, 2) # should print: milk amount in StarBucks: 10, price: 2$
# starbucks.sell('milk') # should print: StarBucks sold milk (1) for 2$
# tesco.sell('milk') # should print: Tesco sold milk (1) for 2.5$
# starbucks.serve_coffee() # should print: StarBucks served coffee for 3$
# print(johndoe.sum_income()) # should print: 19.5
# johndoe.close('McDonalds') # should print: John Doe doesn't have business called McDonalds
# johndoe.close('StarBucks') # should print: John Doe closed StarBucks
# print(johndoe) # should print: John Doe has 1 business(es): Tesco