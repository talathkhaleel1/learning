# GroceryShop

from trail_exam.shop import Shop
from trail_exam.product import Product



class GroceryShop(Shop):
    # can be created by their name
    # should work the same way as a general shop

    def __init__(self, shop_name):
        super().__init__(shop_name)





# when selling, the grocery shops has the opportunity to sell the products \
# with or without a bag. if we choose to buy a bag as well and the selling is successful, \
# we add an additional 1$ as the price of the bag to the income

    def sell(self,product_name, ordered_quantity, sell_with_bag = False):#work the same way as Shop class
        super().sell(product_name, ordered_quantity)# bag attribute given false and sale calculation as per Shop class
        #need to add bag attribute to include it in sale price
        if sell_with_bag == True:
            self.income += 1



