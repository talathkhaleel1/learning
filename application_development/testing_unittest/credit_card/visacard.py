from application_development.test.credit_card.creditcard import CreditCard

class Visa(CreditCard):
    def __init__(self, balance):
        super().__init__('Visa', 0.02, balance)

    def withdraw(self, amount):
        if (amount > self.balance):
            print('Not enough credit.')
            return 0
        self.balance -= amount
        return amount
