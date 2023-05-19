# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

number_of_girls = int(input("please specify the number of girls: "))
number_of_boys = int(input("please specify the number of boys: "))
number_of_people_in_party = number_of_girls + number_of_boys
if number_of_girls == number_of_boys and number_of_people_in_party > 20:
    print("The party is exellent!")
elif number_of_people_in_party > 20 and number_of_girls != number_of_boys:
    print("Quite cool party!")
elif number_of_people_in_party < 20:
    print("Average party")
elif number_of_girls <= 0:
    print("Sausage party")