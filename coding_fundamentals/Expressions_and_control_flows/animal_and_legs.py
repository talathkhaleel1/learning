# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The second represents the number of pigs owned by the farmer
# It should print how many legs all the animals have

number_of_chickens = int(input("Please specify number of chickens: "))
number_of_pigs = int(input("Please specify number of pigs: "))

number_of_legs_each_chicken_has = 2
number_of_legs_each_pig_has = 4

limbs_of_animals = (number_of_chickens * number_of_legs_each_chicken_has)\
                                            +(number_of_pigs * number_of_legs_each_pig_has)
print("Total number of legs all the animals have: ", limbs_of_animals)