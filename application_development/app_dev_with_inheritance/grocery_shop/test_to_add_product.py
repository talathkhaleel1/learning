# Tests
# Write at least 2 unit tests to the add method of a shop.
#
import unittest
from trail_exam.shop import Shop
from trail_exam.product import Product


class TestToAddProduct(unittest.TestCase):

    def test_addProduct_AddsA_Product(self):
    # AAA

# Arrange
        shop = Shop("HyperPanda")# creating shop instance
        item = Product("milk", 5, 5)# creating product instance

#Act
        add_product = shop.add(item, 10, 10)#creating instance with add function of the shop

#Assert
        self.assertEqual(add_product, shop.add("chocolate", 7, 7))


    def test_add_product_UpdatesThe_ListOfProducts(self):
        shop1 = Shop("Mandarin")# Arrange
        product1 = Product("Cheese", 25, 100)

        update_product_details = shop1.add(product1, 30, 300)# Act
        self.assertEqual(update_product_details, shop1.add("Nescafe", 30, 300))# Assert


