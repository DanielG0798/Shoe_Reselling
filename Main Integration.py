"""
This program will help the user store information about the shoe inventory
and perform different tasks with the stock information
The program will also help calculate sales that don't affect the inventory
"""
__author__ = "Daniel Garciamoreno Ortiz"
# This is the inventory I will be tracking
shoe_gender_stock = {'Men': 0, 'Women': 0, 'Unisex': 0}
shoe_size_stock = {'6.0': 0, '6.5': 0, '7.0': 0, '7.5': 0, '8.0': 0, '8.5': 0,
                   '9.0': 0, '9.5': 0, '10.0': 0, '10.5': 0, '11.0': 0,
                   '11.5': 0, '12.0': 0}
shoe_brand_stock = {'Nike': 0, 'Adidas': 0}
shoe_model_stock = {'Jordan': 0, 'Dunk': 0, 'Yeezy': 0}
# I made the list new_inventory to keep track of what was added for the
# session and display it for the user if they need it when pressing 2 on the
# menu
new_inventory = []


# I used this website to help me learn about custom exceptions
# https://www.programiz.com/python-programming/user-defined-exception
class NegativeError(Exception):
    """
    I used class to make my own exception, and it takes in an exception that
    I made an if block that will check if the input is negative
    Pass is used to do nothing else with the exception because the purpose of
    it is just to be used as a custom exception for negative numbers
    :param Exception: If the input is anything else but a positive number, then
    I get an exception
    """
    pass


# I made a function to make it easier to correct wrong
# user input for a number
# Every time I need the user to input a number I use integer_correct()
# Andrew Krupp helped me with the try: except:
# try:
#    variable = int(input())
# except:
#    print("not a valid integer, please try again")
def string_checker(word):
    """
This function is for checking if the user input is a string
by trying to see if the input gives a ValueError when trying to turn it into
an integer when using int(). If there is a ValueError the loop to get only
string input will end and capitalize the first letter of
the string by using the function title()
    :param word: I ask for user input and try to get only a string but the
    string depends on the question asked
    :return: The function returns the user input if it is a string and uses
    the function title() to capitalize the first letter of the word or letter
    """
    some_word = None
    end_loop = True
    while end_loop:
        try:
            some_word = input(word)
            int(some_word)
            print("Please only type words or letters")
        except ValueError:
            return str(some_word).title()


def integer_correct(number):
    """
This function takes the user input and checks to see if it is an integer, it
will only accept a number and does a loop until it gets the correct
input because of the try block. The "if" statement checks if the input is
negative and if so, raises the NegativeError which is a custom
exception I made.
    :param number: I ask for a number input from the user depending on the
    question.
    :return: The function gives back the user input,
    if it is a positive number, and as a float
    """
    exit_loop = False
    while not exit_loop:
        try:
            some_number = float(input(number))
            if some_number < 0:
                raise NegativeError
            # I raise my custom exception here to trigger the except and loop
            # the user back
        except NegativeError:
            print("Please enter only positive numbers")
        except ValueError:
            print("Wrong input, please enter a number")
            continue
        else:
            return some_number


# I used a video to help me have a menu to separate the tasks I want and
# to help me get an idea of how to start an inventory program.
# Source: https://youtu.be/NQn0nAbzdUk
# display_menu is used so that the user can pick between options.
# The user selects their next task with the keyboard input asked.
def display_menu():
    """
This function gives the user input options to choose from by the press
of one of the numbers asked or the letter.
    """
    print("~" * 55)
    # print statement with ("~"*55) just prints 55 '~' symbols
    # I used ~ instead of just having a white space.
    print("Press 1 to add new shoes to the inventory.")
    # 1 is used for adding shoes to the inventory when given the right input
    print("Press 2 to check the current inventory.")
    # 2 spits out the stock numbers for everything
    print("Press 3 to calculate a sell from the current inventory.")
    # 3 is for calculating a sell and subtracting from the stock
    print('Press 4 to start "What if" calculations.')
    # 4 is used for calculating different scenarios depending on the
    # unique sale but for now it calculates popular reselling site fees
    print("Press E to exit Shoe Stock.")
    print("~" * 55)
    # e will end the program
    return input("Type the number or letter for what you want to do: ")


def main():
    """
This function allows the user to run the program when calling main
    """
    # The below print statements print a description of the program
    print("Welcome " + "to " + "Shoe " + "Stock.\n")
    print("This program can help you store information about your shoe\n"
          "inventory as if you were a shoe reseller.\n"
          "The program will also perform different tasks with the stock "
          "information in the future.\n"
          "The program will help calculate sales of shoes in popular reselling"
          "websites\n")
    # The user will input their name, and it will be stored in the variable
    # "user_name" and will have the first letter capitalized by the function
    # title()
    user_name = input("Enter your name: ").title()
    # In this print statement I use {} to insert the contents inside the
    # parentheses of .format() into the string and for this one it is the
    # user input for the variable user_name
    print("Hello, {}".format(user_name))
    run = display_menu()
    # The use of the variable exit to equal true makes a way to break the loop
    # when I make end = False or in this case off = True
    end = True
    off = False
    while end != off:
        if run == "1":
            # I use .format to enter the inputs from the user
            # into some print statements
            # because it makes it easier for me to track.
            print('Hey {}, these questions add shoes to the'
                  ' inventory'.format(user_name))
            shoe_gender = string_checker("Are the shoes Men, Women, or"
                                         " Unisex? ")
            # This while loop will check if the input is what I need
            # it to be to add it
            # in the inventory as well as put the input in the correct
            # format for my list by using the title() function inside
            # the string_checker function
            while shoe_gender not in shoe_gender_stock and \
                    shoe_gender not in ("M", "W", "U"):
                print("Please only enter one of the shoe genders listed")
                shoe_gender = string_checker("Are the shoes Men, Women, "
                                             "or Unisex? ")
            if shoe_gender in ("M", "W", "U"):
                # Here im changing the variable shoe_gender to the way it is
                # stored in the list for shoe_gender_stock, so it can be found
                if shoe_gender == "M":
                    shoe_gender = "Men"
                    shoe_gender_stock[shoe_gender] += 1
                    # I am using the .append to add the contents of the
                    # container into the list new_inventory
                    new_inventory.append("Gender: " + shoe_gender)
                elif shoe_gender == "W":
                    shoe_gender = "Women"
                    shoe_gender_stock[shoe_gender] += 1
                    new_inventory.append("Gender: " + shoe_gender)
                elif shoe_gender == "U":
                    shoe_gender = "Unisex"
                    shoe_gender_stock[shoe_gender] += 1
                    new_inventory.append("Gender: " + shoe_gender)
                    # similar lines like this "shoe_gender_stock[shoe_gender]
                    # += 1" either add or
                    # subtract from the stock, this one adds.
            else:
                shoe_gender_stock[shoe_gender] += 1
                new_inventory.append("Gender: " + shoe_gender)
                # I am turning the input of the shoe_size variable into a
                # string so that it can be detected in the following if else
                # block
            shoe_size = str(integer_correct("Enter the US shoe size: "))
            shoe_size_loop = True
            while shoe_size_loop:
                if shoe_size not in shoe_size_stock:
                    print("Please only enter one of the US shoe sizes in this"
                          " list")
                    print('6.0', '6.5', '7.0', '7.5', '8.0', '8.5',
                          '9.0', '9.5', '10.0', '10.5', '11.0',
                          '11.5', '12.0', sep=',')
                    shoe_size = str(integer_correct("Enter the US shoe "
                                                    "size: "))
                else:
                    if shoe_size in shoe_size_stock:
                        shoe_size_stock[shoe_size] += 1
                        new_inventory.append("Size: " + shoe_size)
                        shoe_size_loop = False
            shoe_brand = string_checker("Is the brand Nike or Adidas? ")
            while shoe_brand not in shoe_brand_stock and \
                    shoe_brand not in ("N", "A"):
                print("Please only enter one of the shoe brands listed")
                shoe_brand = string_checker("Is the brand Nike or Adidas? ")
            if shoe_brand in ("N", "A"):
                # It may become apparent that I am allowing the user to be lazy
                # by catching just one letter that represents what I want.
                # They are capitalized because of the title() function inside
                # my string_checker function which helps format strings to
                # a format that will be like the one in my lists
                if shoe_brand == "N":
                    shoe_brand = "Nike"
                    shoe_brand_stock[shoe_brand] += 1
                    new_inventory.append("Brand: " + shoe_brand)
                elif shoe_brand == "A":
                    shoe_brand = "Adidas"
                    shoe_brand_stock[shoe_brand] += 1
                    new_inventory.append("Brand: " + shoe_brand)
            else:
                shoe_brand_stock[shoe_brand] += 1
                new_inventory.append("Brand: " + shoe_brand)
            shoe_model = string_checker("Is the model Jordan, Dunk, or "
                                        "Yeezy? ")
            while shoe_model not in shoe_model_stock and \
                    shoe_model not in ("J", "D", "Y"):
                print("Please only enter one of the shoe models listed")
                shoe_model = string_checker("Is the model Jordan, Dunk, or "
                                            "Yeezy? ")
            if shoe_model in ("J", "D", "Y"):
                if shoe_model == "J":
                    shoe_model = "Jordan"
                    shoe_model_stock[shoe_model] += 1
                    new_inventory.append("Model: " + shoe_model)
                elif shoe_model == "D":
                    shoe_model = "Dunk"
                    shoe_model_stock[shoe_model] += 1
                    new_inventory.append("Model: " + shoe_model)
                elif shoe_model == "Y":
                    shoe_model = "Yeezy"
                    shoe_model_stock[shoe_model] += 1
                    new_inventory.append("Model: " + shoe_model)
            else:
                shoe_model_stock[shoe_model] += 1
                new_inventory.append("Model: " + shoe_model)
            run = display_menu()

        elif run == "2":
            # key and value are taken from the inventory
            # key being like Men or Nike
            # value being the number in the corresponding key
            print("This is your current inventory\n")
            for key, value in shoe_gender_stock.items():
                # the end = ' ' is for the data to be printed
                # within the same line
                print("{}: {}".format(key, value), end=' ')
            print("")
            for key, value in shoe_size_stock.items():
                print("{}: {}".format(key, value))
            for key, value in shoe_brand_stock.items():
                print("{}: {}".format(key, value), end=' ')
            print("")
            for key, value in shoe_model_stock.items():
                print("{}: {}".format(key, value), end=' ')
            print("\n\nInventory added today\n" + str(new_inventory))

            run = display_menu()

        elif run == "3":

            # resell questions for calculations
            print("Ready to sell? Enter information below")
            print("Only information in the inventory will be accepted here.\n"
                  "If you want to make a sell without affecting the inventory,"
                  " select option 4 in the menu")
            shoe_gender_sell = string_checker('Enter the gender of the shoes:'
                                              ' ')
            while shoe_gender_sell not in shoe_gender_stock and \
                    shoe_gender_sell not in ("M", "W", "U"):
                print("Please only enter Men, Women, or Unisex")
                shoe_gender_sell = string_checker("Are the shoes Men, Women, "
                                                  "or Unisex? ")
            if shoe_gender_sell in ("M", "W", "U"):
                if shoe_gender_sell == "M":
                    shoe_gender_sell = "Men"
                    shoe_gender_stock[shoe_gender_sell] -= 1
                elif shoe_gender_sell == "W":
                    shoe_gender_sell = "Women"
                    shoe_gender_stock[shoe_gender_sell] -= 1
                elif shoe_gender_sell == "U":
                    shoe_gender_sell = "Unisex"
                    shoe_gender_stock[shoe_gender_sell] -= 1
            else:
                shoe_gender_stock[shoe_gender_sell] -= 1
            shoe_brand_sell = string_checker("Enter the brand: ")
            while shoe_brand_sell not in shoe_brand_stock and \
                    shoe_brand_sell not in ("N", "A"):
                print("Please only enter Nike or Adidas")
                shoe_brand_sell = string_checker("Is the brand Nike or "
                                                 "Adidas? ")
            if shoe_brand_sell in ("N", "A"):
                if shoe_brand_sell == "N":
                    shoe_brand_sell = "Nike"
                    shoe_brand_stock[shoe_brand_sell] -= 1
                elif shoe_brand_sell == "A":
                    shoe_brand_sell = "Adidas"
                    shoe_brand_stock[shoe_brand_sell] -= 1
            else:
                shoe_brand_stock[shoe_brand_sell] -= 1
            shoe_model_sell = string_checker("Enter the model: ")
            while shoe_model_sell not in shoe_model_stock and \
                    shoe_model_sell not in ("J", "D", "Y"):
                print("Please only enter Jordan, Dunk, or Yeezy")
                shoe_model_sell = string_checker("Is the model Jordan, Dunk, "
                                                 "or Yeezy? ")
            if shoe_model_sell in ("J", "D", "Y"):
                if shoe_model_sell == "J":
                    shoe_model_sell = "Jordan"
                    shoe_model_stock[shoe_model_sell] -= 1
                elif shoe_model_sell == "D":
                    shoe_model_sell = "Dunk"
                    shoe_model_stock[shoe_model_sell] -= 1
                elif shoe_model_sell == "Y":
                    shoe_model_sell = "Yeezy"
                    shoe_model_stock[shoe_model_sell] -= 1
            else:
                shoe_model_stock[shoe_model_sell] -= 1
            shoe_size_sell = str(integer_correct("Enter the US size: "))
            shoe_size_loop = True
            while shoe_size_loop:
                if shoe_size_sell not in shoe_size_stock:
                    print("Please only enter one of the US shoe sizes in this"
                          " list")
                    print('6.0', '6.5', '7.0', '7.5', '8.0', '8.5',
                          '9.0', '9.5', '10.0', '10.5', '11.0',
                          '11.5', '12.0', sep=',')
                    shoe_size_sell = str(integer_correct("Enter the US shoe "
                                                         "size: "))
                else:
                    if shoe_size_sell in shoe_size_stock:
                        shoe_size_stock[shoe_size_sell] += 1
                        shoe_size_loop = False
            retail_price = integer_correct("What is the retail price? $")
            estimated_resell = integer_correct("What is the estimated "
                                               "resell price? $")
            print('\nResults')
            print("-" * 7)
            profit = estimated_resell - retail_price
            print('Gender: {}\nBrand: {}\nModel: {}\nSize: {}\n'
                  .format(shoe_gender_sell, shoe_brand_sell, shoe_model_sell,
                          shoe_size_sell))
            print("Estimate: $", format(profit, ".2f"), sep='')
            # The sep='' is adding space in between the string and the format
            # gives me 2 decimal places
            # I have included a message for the user using if,elif,else
            # depending on if there is profit, break even, or no profit
            # based on the value in variable profit
            if profit > 0:
                print("Profit was made")
            elif profit == 0:
                print("Break even")
            else:
                print("No profit made")
            run = display_menu()

        elif run == "4":
            # The + is being used to stick strings together
            print('This' + ' ' + 'is' + ' ' + '"What'
                                              ' if"' + ' ' + 'calculations')
            
            print(
                '"What if"', "won't", "affect", "the", "stock.")
            number_of_shoes = int(integer_correct("How many of the same "
                                                  "kind of shoe will "
                                                  "be sold? "))
            shoe_retail = integer_correct("Enter the retail price: ")
            resell = integer_correct("Enter the resell price: ")
            # 3 to the power of 2 is written with ** and is used here to get 9
            # I am adding the results in the parenthesis with +
            calc1 = (3 ** 2) + (6 // 2) + (1 / 2)
            # The floor division // gets the integer that is 8 out of 100/12
            # and takes away the remainder
            # I used the floor division here to get 8 because it is needed for
            # the ebay fee
            calc2 = (100 // 12)
            # I multiply two variables that are meant to
            # be numbers to get a product
            calc3 = number_of_shoes * shoe_retail
            calc4 = resell * number_of_shoes
            # The modulus % gets me a 1 because 5/4 leaves a remainder of 1.25
            # and leaves the decimals behind
            profit_no_fees = (calc4 - calc3) * (5 % 4)
            # I'm subtracting with - to get the profit calculations
            ebay_fees = (calc4 - calc3) * (calc2 / 100)
            # I divide with / to get decimals in order to calculate percentage
            stockx_fees = (calc4 - calc3) * (12 / 100)
            goat_fees = (calc4 - calc3) * (calc1 / 100)
            ebay_fees1 = (profit_no_fees - ebay_fees)
            stockx_fees1 = (profit_no_fees - stockx_fees)
            goat_fees1 = (profit_no_fees - goat_fees)
            print("\nResults")
            # print("-"*7) adds a separation with 7 of the - lines
            print("-" * 7)
            # I format each print statement so that the variable
            # has 2 decimal places with .2f and use sep='' to remove
            # the spacing between the string $ and the number variables
            print("No Fees: $", format(profit_no_fees, ".2f"), sep='')
            print("Stockx fees included: $", format(stockx_fees1,
                                                    ".2f"), sep='')
            print("Ebay fees included: $", format(ebay_fees1, ".2f"), sep='')
            print("Goat fees included: $", format(goat_fees1, ".2f"), sep='')

            run = display_menu()

        elif run == "e" or run == "E":
            # the for i in range creates a countdown by using -1 in
            # the third value
            for i in range(3, 0, -1):
                print(i)
            off = True
        else:
            print("Invalid choice, try again")

            run = display_menu()

    print("Your session has ended")


if __name__ == "__main__":
    main()
# Notes on future code
# To be used later   cut = input('Any division of profit? if not enter "No"')
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
# Source that helped me understand the loop
# www.includehelp.com/python/asking-the-user-for-input-until-a-
# valid-response-in-python.aspx
# while True:
#       try:
#          fees = input('Enter "Yes" to calculate 3rd party fees, \
#               if not enter "No": ')
#          if fees == "Yes" or fees == "yes":
#              stockx_fee = (12/100)
#              print("Stockx fee is 12%")
#              break;
#          elif fees == "No" or fees == "no":
#              print("No fees")
#              break;
#          elif fees != (fees == "Yes" or fees == "yes") or
#       (fees == "No" or fees == "no"):
#              print("try again")
#      except:
#          continue
# user_options = string_checker("Type yes to continue or no for "
#                               "the menu: ")
# user_loop = True
# while user_loop:
#     if user_options not in ("Y", "N", "Yes", "No"):
#         print("Please only enter Yes or No")
#         user_options = string_checker("Type yes to continue or no"
#                                       " for the menu: ")
#     elif user_options in ("Y", "Yes"):
#         user_loop = False
#     elif user_options in ("N", "No"):
#         user_loop = False
