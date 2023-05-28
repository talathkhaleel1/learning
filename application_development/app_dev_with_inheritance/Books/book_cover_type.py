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

class HardCover(Book):
   def __init__(self, author, title, price, cover_price = 100):
       super().__init__(author, title, price + cover_price)
       self.coverPrice = cover_price

class PaperCover(Book):
   def __init__(self, author, title, price):
       super().__init__(author, title, price)
   def sell(self, money):
       print(max(money - self.price, 0))

from application_development.trial_test.book import Book
from application_development.trial_test.hardcover import HardCover
from application_development.trial_test.papercover import PaperCover

lotr = HardCover('J.R.R. Tolkien', 'The Lord of the Rings: The Fellowship of the Ring', 1000)
hp = HardCover('J.K. Rowling', "Harry Potter and the Philosopher's Stone", 1000, 200)
lp = PaperCover('Antoine de Saint-Exupéry', "The Little Prince", 1000)
lotr.sell(1200)
hp.sell(1200)
lp.sell(1200)
