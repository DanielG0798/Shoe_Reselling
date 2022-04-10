#Daniel Garciamoreno Ortiz
#This program will help the user store information about shoe inventory
#and perform different tasks with the stock information
#the program will also help me in the future to calculate different
#transactions that can happen in different situations.
##The numbers below that are commented out will be used in the future.
##'6': 0,'6.5': 0,'7': 0,'10.5': 0,'11': 0,'11.5': 0,'12': 0

#This is the inventory I will be tracking for now
shoe_gender_stock = {'Men': 0,'Women': 0,'Unisex': 0}
shoe_size_stock = {'7.5': 0,'8.0': 0,'8.5': 0,'9.0': 0,'9.5': 0,'10.0': 0}
brand_stock= {'Nike': 0,'Adidas': 0}
model_stock = {'Jordan': 0,'Dunk': 0,'Yeezy': 0}

#I used this website to help me learn about custom exceptions
# https://www.programiz.com/python-programming/user-defined-exception
class negative_error(Exception):
    pass
#I made a function to make it easier to correct wrong
#user input for a number
#Every time I need the user to input a number I use integer()
##Andrew Krupp helped me with the try: except:
##try:
##    variable = int(input())
##except:
##    print("not a valid integer, please try again")
def integer(number):
    exit = True
    while not exit != True:
        try:
           some_number = float(input(number))
           if some_number < 0:
               raise negative_error
        except negative_error:
            print("Please enter only positive numbers")
        except ValueError:
            print("Wrong input, please enter a number")
            continue
        else:
            return some_number

#These are welcome prompts for the user and I used the + sign to get
#two strings to be stuck together.
print("Welcome "+"to "+"Shoe "+"Stock.\n\n")
user_name = input("Enter your name: ")
print("Hello, {}".format(user_name))

#I used a video to help me have a menu to separate the tasks I want and
#to help me get an idea of how to start an inventory program.
#Source: https://youtu.be/NQn0nAbzdUk
##menu is used so that the user can pick between set tasks.
###The user selects their next task with the keyboard.
def menu():
    print("~"*55)
#print statement with ("~"*55) just prints 55 '~' symbols
#I used ~ instead of just having a white space.
    print("Press 1: Add new shoes to stock.")
#1 is used for adding shoes to the inventory when given the right input
    print("Press 2: Check current stock.")
#2 spits out the stock numbers for everything
    print("Press 3: Calculate a sell from current stock.")
#3 is for calculating a sell and subtracting from the stock
    print('Press 4: Start "What if" calculations.')
#4 is used for calculating different scenarios depending on the unique sale
    #for now it calculates popular reselling site fees
    print("Press e: Exit Shoe Stock.")
    print("~"*55)
#e will end the program
    return input("What would you like to do? ")
#return will allow the user to go into the menu based on their input


run = menu()
#The use of the variable exit to equal true makes a way to break the loop
#when I make exit = False
end = True
off = False
while end != off:
    if run == "1":
#I use .format to enter the inputs from the user into the print statement
#because it makes it easier for me to track.
        print("Hey {}, these questions add shoes to stock".format(user_name))
        shoe_gender = input("Are the shoes Men, Women, or Unisex? ")
#This while loop will check if the input is what I need it to be to add it
#in the inventory as well as put the input in the correct format for my list
#by using the capitalize() and title() functions
        while shoe_gender not in shoe_gender_stock and shoe_gender not in \
                ("men","MEN","women","WOMEN","unisex","UNISEX"):
            print("Please only enter one of the shoe genders listed")
            shoe_gender = input("Are the shoes Men, Women, or Unisex? ")
            if shoe_gender in ("men","women","unisex"):
                shoe_gender_cap = shoe_gender.capitalize()
#similar lines like this "shoe_gender_stock[shoe_gender] += 1" either add or
#subtract from the stock, this one adds.
                shoe_gender_stock[shoe_gender_cap] += 1
            elif shoe_gender in ("MEN","WOMEN","UNISEX"):
                shoe_gender_cap = shoe_gender.title()
                shoe_gender_stock[shoe_gender_cap] += 1
        shoe_size = str(integer("Enter the US shoe size: "))
        if shoe_size in shoe_size_stock:
            shoe_size_stock[shoe_size] += 1
        else:
            print('{} will not be stored in the stock'.format(shoe_size))
        shoe_brand = input("Is the brand Nike or Adidas? ")
        if shoe_brand in brand_stock:
            brand_stock[shoe_brand] += 1
        else:
            print('{} will not be stored in the stock'.format(shoe_brand))
        shoe_model = input("Is the model Jordan, Dunk, or Yeezy? ")
        if shoe_model in model_stock:
            model_stock[shoe_model] += 1
        else:
            print('{} will not be stored in the stock'.format(shoe_model))
        run = menu()
 
    elif run == "2":
        #key and value are taken from the inventory key being like Men or Nike
        #value being the number in indicated stock for the corresponding key
        print("Check in on your shoes")
        for key, value in shoe_gender_stock.items():
            #the end = ' ' is for the data to be printed within the same line
            print("{}: {}".format(key, value),end=' ')
        for key, value in shoe_size_stock.items():
            print("\n{}: {}".format(key, value))
        for key, value in brand_stock.items():
            print("{}: {}".format(key, value),end=' ')
        for key, value in model_stock.items():
            print("\n{}: {}".format(key, value))
            print("")
        run = menu()

    elif run == "3":

 #resell questions for calculations
        print("Ready to sell? Enter information below")
        shoe_gender1 = input('Enter "Male", "Female", or "Unisex": ')
        while shoe_gender1 not in shoe_gender_stock and shoe_gender1 not in \
                ("men", "MEN", "women", "WOMEN", "unisex", "UNISEX"):
            print("Please only enter one of the shoe genders listed")
            shoe_gender1 = input("Are the shoes Men, Women, or Unisex? ")
            if shoe_gender1 in ("men", "women", "unisex"):
                shoe_gender_cap = shoe_gender1.capitalize()
                shoe_gender_stock[shoe_gender_cap] -= 1
            elif shoe_gender1 in ("MEN", "WOMEN", "UNISEX"):
                shoe_gender_cap = shoe_gender1.title()
                shoe_gender_stock[shoe_gender_cap] -= 1
        shoe_brand1 = input("Enter the brand: ")
        shoe_model1 = input("Enter the model: ")
        shoe_size1 = str(integer("Enter the size: "))
        retail_price = integer("What is the retail price? $")
        estimated_resell = integer("What is the estimated \
resell price? $")
        print('\nResults')
        print("-"*7)
        profit = estimated_resell - retail_price

        if shoe_brand1 in brand_stock:
            brand_stock[shoe_brand1] -= 1
        else:
            print('{} is not in stock'.format(shoe_brand1))
        if shoe_model1 in model_stock:
            model_stock[shoe_model1] -= 1
        else:
            print('{} is not in stock'.format(shoe_model1))
        if shoe_size1 in shoe_size_stock:
            shoe_size_stock[shoe_size1] -= 1
        else:
            print('{} is not in stock'.format(shoe_size1))
        print('Gender: {}\nBrand: {}\nModel: {}\nSize:/ {}\n'
            .format(shoe_gender1, shoe_brand1, shoe_model1, shoe_size1))
        print("Estimate: $",format(profit, ".2f"),sep='')
 #I have included a message for the user using if,elif,else
        if profit > 0:
            print("Profit was made")
        elif profit == 0:
            print("Break even")
        else:
            print("No profit made")
        run = menu()

    elif run == "4":
        #The + is being used to stick strings together
        print('This'+' '+'is'+' '+'"What if"'+' '+'calculations')
        #The sep= ' ' is adding space where the commas are in between
        #each string
        print('"What if"',"won't","affect","the","stock.",sep=' ')
        number_of_shoes = int(integer("How many of the same kind of \
shoe will be sold? "))
        shoe_retail = integer("Enter the retail price: ")
        resell = integer("Enter the resell price: ")
        #3 to the power of 2 is written with ** and is used here to get 9
        #I am adding the results in the parenthesis with +
        calc1 = (3**2) + (6//2) + (1/2)
        #The floor division // gets the integer that is 8 out of 100/12
        #and takes away the remainder
        #I used the floor division here to get 8 because it is needed for
        #the ebay fee
        calc2 = (100//12)
        #I multiply two variables that are meant to
        #be numbers to get a product
        calc3 = number_of_shoes * shoe_retail
        calc4 = resell * number_of_shoes
        #The modulus % gets me a 1 because 5/4 leaves a remainder of 1.25
        #and leaves the decimals behind
        profit_no_fees = (calc4 - calc3)*(5%4)
        #I'm subtracting with - to get the profit calculations
        ebay_fees = (calc4 - calc3)*(calc2/100)
        #I divide with / to get decimals in order to calculate percentage
        stockx_fees = (calc4 - calc3)*(12/100)
        goat_fees = (calc4 - calc3)*(calc1/100)
        ebay_fees1 = (profit_no_fees - ebay_fees)
        stockx_fees1 = (profit_no_fees - stockx_fees)
        goat_fees1 = (profit_no_fees - goat_fees)
        print("\nResults")
        #print("-"*7) adds a separation with 7 of the - lines
        print("-"*7)
        #I format each print statement so that the variable
        #has 2 decimal places with .2f and use sep='' to remove
        #the spacing between the string $ and the number variables
        print("No Fees: $",format(profit_no_fees,".2f"),sep='')
        print("Stockx fees included: $",format(stockx_fees1,".2f"),sep='')
        print("Ebay fees included: $",format(ebay_fees1,".2f"),sep='')
        print("Goat fees included: $",format(goat_fees1,".2f"),sep='')
        
        run = menu()
        
    elif run == "e" or run == "E":
        #the for i in range creates a countdown by using -1 in the third value
        for i in range(3, 0, -1):
            print(i)
        off = True
    else:
        print("Invalid choice, try again")
        run = menu()

print("Your session has ended")


## to be used later   cut = input('Any division of profit? if not enter "No"')
#        exit = True
#        while exit == True:
#                fees = input('Enter "Yes" to calculate 3rd party fees,\
#                if not enter "No": ')
#               if fees == "Yes" or fees == "yes":
#                   stockx_fee = (12/100)
#                   print("Stockx fee is 12%")
#                   exit = False
#               elif fees == "No" or fees == "no":
#                   print("No fees")
#                   exit = False
## Personal note of what else could work
#Source that helped me understand the loop
#www.includehelp.com/python/asking-the-user-for-input-until-a-
# valid-response-in-python.aspx
##while True:
##      try:
##          fees = input('Enter "Yes" to calculate 3rd party fees, \
#               if not enter "No": ')
##          if fees == "Yes" or fees == "yes":
##              stockx_fee = (12/100)
##              print("Stockx fee is 12%")
##              break;
##          elif fees == "No" or fees == "no":
##              print("No fees")
##              break;
##          elif fees != (fees == "Yes" or fees == "yes") or
#       (fees == "No" or fees == "no"):
##              print("try again")
##      except:
##          continue
