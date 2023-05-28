from application_development.trial_test.book import Book

class HardCover(Book):
   def __init__(self, author, title, price, cover_price = 100):
       super().__init__(author, title, price + cover_price)
       self.coverPrice = cover_price