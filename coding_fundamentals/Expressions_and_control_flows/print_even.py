# Create a program that prints all the even numbers between 0 and 500

count_limit = int(input("What is the count limit you desire?"))
for i in range(count_limit):
    if i % 2 == 0:
        print(i)