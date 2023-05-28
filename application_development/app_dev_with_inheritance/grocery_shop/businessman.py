
# BusinessMan
#
# To keep it simple, our application should be able to handle only shops as businesses.

from trail_exam.shop import Shop

class BusinessMan:

    type = "Business"

    # can be created by their name
    def __init__(self, name):
        self.name = name
        self.list_of_business = []


    # def get_business_name(self, name, list_of_business):
    #     for business in self.list_of_business:
    #         if business == name:
    #             return business

# can add a new business to their portfolio

    def add(self, business):
        self.list_of_business.append(business)


    # can close one of their business

    def close(self, business_to_close):
        index_of_business_to_close = -1 # suppose we are closing the last business
        for i in range(len(self.list_of_business)):
            if self.list_of_business[i]== index_of_business_to_close:
                index_of_business_to_close = i
                break
        if index_of_business_to_close != -1:# when we are not closing last business but some other business
            self.list_of_business.remove(self.list_of_business[index_of_business_to_close])
            print(business_to_close.get_business_detail() + "successfully closed")
        else:
            print("No such business found in " + self.list_of_business.index([i]) + "business list.")

    # can count the sum income of their businesses # need to ask this to Sir
    def sum_income(self):
        self.income = float
        self.income += Shop.income()
        income_of_all_businesses = len(self.income.sum())# trying to add income of  all businesses
        return income_of_all_businesses

    # «name» has «number of businesses» business(es): «business 1 name», ..., «business n name»
    #is represented in the following format

    def __str__(self):
        businessman_detail = self.name + " has " + str(len(self.list_of_business)) + " business(es) : "
        for business in self.list_of_business:
            businessman_detail += business.shop_name# how to insert business name here???
            return businessman_detail

