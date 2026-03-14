class Card:

    def __init__(self, num, col):
        self.__Number = num
        self.__Colour = col

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour

card_array = []             # the data type will be card

try:
    file = open("CardValues.txt", "r")
except IOError:
    print("File not found")
    
for i in range(30):
    card_array.append(Card(0, ''))