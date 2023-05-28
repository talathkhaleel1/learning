class CountEven:

    def count_even(number):
        number= 11
        if 0 >= number or number > 100:
            return 0                        # here we set the range for the the numbers within which we need /
        if 0 < number:                      # to count the number of even numbers
            count = 0                       # count given default value for now but is incremented
            for i in range (1, number):
                if i % 2 == 0:              # divisibility rule for ven number
                    count += 1              #everytime above rule is satisfied the count is incremented by 1
            return count                    # return the counts