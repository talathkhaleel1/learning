from application_development.test.credit_card.creditcard import CreditCard


class MasterCard(CreditCard):
    def __init__(self, balance):
        super().__init__('MasterCard', 0.01, balance) # no abstraction so withdraw rule of the parent class