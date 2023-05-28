# Write a zoo management program. We want to register new zoos in the system. /
# Every zoo has a name and the size of its territory. The territory of a zoo is by default 100.
#
# We want to place animals in zoos. Every animal has a name and a /
# territory requirement (the amount of territory the animal needs to live). /
# The territory requirement of an animal is by default 20.
#
# When a zoo has enough free territory for the animal which we want to place there, then the zoo places the animal.
#
# We also want to sell animals from a zoo to free up some territory to other animals. /
# A zoo always sells the animal which requires the most territory. When a zoo sells an animal, /
# it returns the sold animal and frees up its territory to be able to place new animals.
#
# Using your solution, the following code should run without errors and print the expected results.

from application_development.trial_test.animals import Animals

class Zoo:

    def __init__(self, name, size_of_territory = 100):
        self.name= name
        self.size_of_territory = size_of_territory

