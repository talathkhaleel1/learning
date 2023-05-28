# Create Sharpie class
# We should know about each sharpie their color (which should be a string), /
#       width (which will be a floating point number),/
#       ink_amount (another floating point number)
# When creating one, we need to specify the color and the width
# Every sharpie is created with a default 100 as ink_amount
# We can use() the sharpie objects
#       which decreases inkAmount

class Sharpie:

    def __init__(self, color, width):
        self.color : str = color
        self.width : float = width
        self.ink_amount : float = 100

    def __str__(self):
        return "colour: "+self.color +" "+"width: "+str(self.width)

    def sharpie(self):
        self.ink_amount -= 1

