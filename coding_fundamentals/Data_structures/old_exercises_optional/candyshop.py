# shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called sweets() which takes the list as a parameter.
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"

shop_items = ["Cupcake", 2, "Brownie", False]


def sweets(list):
    for i in range(len(list)):
        if list[i] == 2:
            list[i] = "Croissant"
        elif list[i] == False:
            list[i] = "Ice Cream"
    return list

print(sweets(shop_items))

