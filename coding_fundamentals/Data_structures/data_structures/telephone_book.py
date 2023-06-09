# We are going to represent our contacts in a map where the keys are going to be strings\
# and the values are going to be strings as well.
#
# Create a map with the following key-value pairs.
#
# Name (key)	Phone number (value)
# William A. Lathan	405-709-1865
# John K. Miller	402-247-8568
# Hortensia E. Foster	606-481-6467
# Amanda D. Newland	319-243-5613
# Brooke P. Askew	307-687-2982
# Create an application which solves the following problems.
#
# What is John K. Miller's phone number?
# Whose phone number is 307-687-2982?
# Do we know Chris E. Myers' phone number?

telephone_book = {"William A. Lathan":"405-709-1865", "John K. Miller":"402-247-8568",\
                  "Hortensia E. Foster":"606-481-6467", "Amanda D. Newland":"319-243-5613",\
                   "Brooke P. Askew":"307-687-2982"}

# What is John K. Miller's phone number?
print("John K. Miller's phone number is :", telephone_book["John K. Miller"])

# Whose phone number is 307-687-2982?
for k,v in telephone_book.items():
    if v == "307-687-2982":
        print("This phone number belongs to :", k)

# Do we know Chris E. Myers' phone number?
print("Chris E. Myers'" in telephone_book)# returns boolean values

