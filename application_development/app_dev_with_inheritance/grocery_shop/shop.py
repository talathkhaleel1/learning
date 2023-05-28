# Shop
from trail_exam.product import Product

class Shop:
    # can be created by their name


    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.list_of_products = []
        self.income = 0

    def __str__(self):
        print(self.shop_name)

# can add new product to its store by giving the quantity and the price (per unit) of the product

    # when we successfully added a product to a shop, we should \
    # print:  «product name» amount in «shop name»: «product quantity», price: «product price»$
    # if the shop already has this product and we provide a new price on addition,\
    # beside adding the products to the store, we should update the price of the product as well\
    # to the given price. except if the given price is lower than the previous one, \
    # in this case we should keep the previous price (a price of a product can never be lower \
    # in a shop than it was previously)

    # if the shop already had this product, giving its price is optional, \
    # if price is not given, we should use the previous price

    # if the shop hasn't got this product yet, giving the price on addition is mandatory.\

    # If no price is given, then we shouldn't add the products to the store and \
    # print: «product name» can't be added to «shop name» without a price

    def add(self, product_name, quantity, price = 0):
        item_found = False
        for product in self.list_of_products:
            if product.name == product_name:
                new_price = price
                if new_price < product.price and new_price != 0:
                    new_price = product.price # do I write self.price here
                item_found = True
                product1 = Product(product_name, quantity, new_price)
                self.list_of_products.append(product1)
                print(product_name + "amount in "+ self.shop_name + " : "+ quantity+ ", price: "+new_price + "$")
        if item_found == False and price == 0:
            print(product_name + " can't be added to " + self.shop_name + " without a price.")


# can sell products by giving the name and quantity of the product that we'd like to sell

    # if the given product is not in the shop, then we should print: There's no «product name» \
    # in «shop name»

    # if there's not enough product in the shop, we shouldn't sell any, but print:
    # «shop name» doesn't have enough «product name», only «product quantity» available

    # if the shop has the product in the required quantity, we should decrement the quantity \
    # from the store and increment the income of the shop by the sum price of the products.\
    # We should also print:«shop name» sold «product name» («sold quantity») for «sum sold price»$

    def sell(self, product_name, order_quantity): #sell specifying name and quantity
        item_found = False
        for product in self.list_of_products:
            if product.name == product_name: # if product name in product list
                item_found = True
                if product.quantity < order_quantity:# if available quantity less than order quantity no sales
                    print(self.shop_name+ " doesn't have enough " +product_name+ " only "+\
                       product.quantity + "available. ")
                else:# if available quantity more than or equal to order quantity then sell
                    product.quantity -= order_quantity#reduce available quantity by the sale quantity
                    self.income += order_quantity * product.price #calculate sale amount
                    print(self.shop_name+ " sold "+ product_name + " of " + order_quantity+\
                       " for "+self.income + "$")#acknowledge sales
        if item_found == False:# If product name not in product list
            print("There's no " + product_name + " in " + self.shop_name)

