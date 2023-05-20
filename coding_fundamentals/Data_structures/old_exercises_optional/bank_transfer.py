# accounts = [
# 	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
# 	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
# 	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
# ]

# Create function that returns the name and balance of cash on an account in a list
# get_name_and_balance(accounts, 11234543)
# The output should be: "Igor", "203004099.2"



accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]


def get_name_and_balance(account_number):
    # Optional: security feature - return if input is not a number
    if not isinstance(account_number, int):
        return
    # Iterate through every item (dictionary) in the list
    for i in range(len(accounts)):   # first unpack dictionary from list
        account_detail = accounts[i]   # get the actual dicionary
        # Check if in the given dictionary the "account_number" key equals account_number (get a value for a key)
        actual_account_number = account_detail['account_number']
        # Check if the actual account has the number we need
        if actual_account_number == account_number:
            return [account_detail["client_name"], account_detail["balance"]]


print(get_name_and_balance(23456311))

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def transfer_amount(from_account_number, to_account_number, amount_to_transfer):
    from_account_exist = False
    to_account_exist = False
    for i in range(len(accounts)): # first unpack dictionary from list
        account_detail = accounts[i]
        if from_account_number == account_detail["account_number"]:
            from_account_exist = True
            if account_detail["balance"] >= amount_to_transfer:
               account_detail["balance"] -= amount_to_transfer # reduce balance by amount to transfer
        elif to_account_number == account_detail["account_number"]:
            to_account_exist = True
            account_detail["balance"] += amount_to_transfer  # increase balance by amount to transfer
    if from_account_exist == False or to_account_exist == False:
        print("404 - account not found")

transfer_amount(11234543, 43546731, 999)

