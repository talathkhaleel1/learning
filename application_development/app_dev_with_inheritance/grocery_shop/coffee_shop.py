# CoffeeShop


from trail_exam.shop import Shop
class CoffeeShop(Shop):

# can be created by their name and the price of its served coffee
#
# should work the same way as a general shop

    def __init__(self, shop_name, price):
        super().__init__(shop_name)
        self.price = price

# can serve coffee as well on the given price
#
# when a coffee is served, the price of the coffee is added to the income of the shop,\
# and we print: «shop name» served coffee for «coffee price»$

    def serve_coffee(self, product_name, quantity):
        super().sell(product_name, quantity)
        coffee_served = quantity * self.price
        self.income += coffee_served  # the price of the coffee is added to the income of the shop
        print(self.shop_name+ " served coffee for "+ self.price + " $.")

