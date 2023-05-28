# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program

class Counter:

    def __init__(self):
        self.counter :int = 0 # we are not writing it in the parameter next to self because default value is specified.

    def __str__(self):
        return "counter1= " + str(self.counter) +" "+"counter2= " +str(self.counter)


    def __add__(self, other):
        self.counter += other

    def add(self):
        self.counter += 1

    def get_current_value(self):
        self.counter

    def reset_value(self):
        self.counter -= self.counter


