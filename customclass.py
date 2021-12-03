""" 
Alexis Huang
Custom Class Assignment; implementing my own class based on a real world object: Drinks
Sources: Used ultimate fruit basket example
"""
# Creating a class for drinks
class Drinks:
    # __init__ method to initialize
    def __init__(self, brandname=None, flavor=None, container='can', amount_oz=0):
        # public variables
        self.brandname = brandname
        self.flavor = flavor
        self.container = container
        self.amount_oz = amount_oz
        # private variables
        self.__alcoholic = False
        self.__alcoholcontent = 0
        self.__price = 0
    
    # set method to set the drink's brand, flavor, and amount
    # these can be set through the __init__ variables as well, but I like being able to input the info this way
    def setdrink(self):
        # setting the brand
        self.brandname = input("What brand is your drink from? \n>>> ")
        # setting the flavor
        self.flavor = input("What flavor is your drink? \n>>> ")
        # setting the size of the drink
        self.amount_oz = float(input("How many ounces is your drink? \n>>> "))
    
    # set method to set the price of the drink
    # place the price as the input variable
    def setprice(self, price):
        self.__price = price
        # floating the price to make things easier
        price = float(price)
    
    # get method for the price    
    def getprice(self):
        # returns the price of the drink rounded to 2 decimal places
        return str(f'Your drink costs ${self.__price:.2f}.')
    
    # method to switch between container types    
    def switchcontainer(self):
        # if the container is a can, switch to a bottle
        if self.container == 'can':
            self.container = 'bottle'
        # if the container is a bottle, switch to a can
        elif self.container == 'bottle':
            self.container = 'can'
            
    # method to add alcohol (only if ur 21 or older)
    def addalcohol(self):
        # asking for age
        age = int(input("How old are you? \n>>> "))
        # if under 21, drink cannot be alcoholic
        if age < 21:
            print (f"You're {age} years old. Your drink cannot be alcoholic.")
            # set alcoholic to false
            self.__alcoholic = False
        # if over 21, ask if they want to add alcohol to drink
        else:
            want_alcohol = input("Would you like to add alcohol to your drink? \n>>> ")
            if want_alcohol == 'yes':
                # if yes set alcoholic to true
                self.__alcoholic = True
                # ask how many ounces to add to calculate alcohol content
                alcoholounces = float(input("How many ounces of alcohol are you adding? \n>>> "))
                # the total ounces of the drink is original amount plus the added alcohol amount
                totaldrinkoz = float(self.amount_oz) + alcoholounces
                # the alcohol content is the percent of alcohol within the total amount
                self.__alcoholcontent = alcoholounces / totaldrinkoz
            # if no want alcohol then alcoholic is false
            elif want_alcohol == 'no':
                self.__alcoholic = False
    
    # get method to see if drink is alcoholic            
    def getalcoholic(self):
        # if true then return string saying there is alcohol
        if self.__alcoholic == True:
            return str(f'You added alcohol to your drink.')
        # if false then return string saying there is not
        if self.__alcoholic == False:
            return str(f'You did not add alcohol to your drink.')
    
    # print description of drink; brand, flavor, original container amount and type, whether or not it is alcoholic, the alcohol content (0% if non alcoholic), total price
    def __str__(self):
        print (f"Your drink: \n\tBrand: {self.brandname} \n\tFlavor: {self.flavor} \n\tContainer: {self.amount_oz} oz. {self.container} \n\tAlcoholic: {self.__alcoholic} \n\tAlcohol Content: {self.__alcoholcontent:.2f}% \n\tTotal Price: \n\t\t${self.__price:.2f}")
    
# main function
def main():
    yourdrink = Drinks()
    yourdrink.setdrink()
    yourdrink.setprice(3.5)
    print(yourdrink.getprice())
    yourdrink.switchcontainer()
    yourdrink.addalcohol()
    print(yourdrink.getalcoholic())
    yourdrink.__str__()
    

   
if __name__ == "__main__":
    main()