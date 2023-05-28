from application_development.trial_test.book import Book

class PaperCover(Book):
   def __init__(self, author, title, price):
       super().__init__(author, title, price)
   def sell(self, money):
       print(max(money - self.price, 0))
