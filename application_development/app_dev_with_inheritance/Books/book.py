class Book:
   print_number = 1
   def __init__(self, author, title, price):
       self.author = author
       self.title = title
       self.price = price
       if Book.print_number <= 1:
           self.price *= 2
       Book.print_number += 1
   def sell(self, money):
       print(money - self.price if money >= self.price else money)
