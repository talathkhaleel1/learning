class CreditCard:
    def __init__(self, provider, transaction_fee, balance=0):
        self.provider = provider
        self.transaction_fee = transaction_fee
        self.balance = balance

    def withdraw(self, amount):
        fee = amount * self.transaction_fee
        if amount + fee > self.balance:
            print('Not enough credit.')
            return 0
        self.balance -= amount + fee
        return amount