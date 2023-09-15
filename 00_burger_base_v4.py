import random


# functions
# makes names capitals so is grammatically correct
def capitalize_name(name):
    if not name:
        return ""

    # Convert the first character to uppercase and the rest to lowercase
    capitalized = name[0].upper() + name[1:].lower()
    return capitalized


# instructions and the menu
def show_instructions():
    print('''\n
---- Troy's Big Burgers ----

---- Menu ----

BURGERS

BEEF

Classic Cheese $12.50 (cheese)
Big Bacon Burger $17.50 bacon)

CHICKEN

Cheesy Chicken $15 (chicken)

VEGAN

Exquisite Vegan $14 (vegan)

------ Instructions ------

-Enter your name

For each Burger order...
- Type the corresponding word in the brackets on the right into the input box.
 eg: if you want a Classic Cheese type cheese 
- Select a payment method (cash / credit)

When you have entered all the Burgers, press 'xxx' to finalise order.

The program will then display the order details
including the cost of each burger, the chosen sides
and the total profit.


------------------------------------------------------------------------------------------------------''')


def show_prize():
    print('''\n
------ Giveaway ------

You have entered our monthly giveaway!!!
   - This months prize is a $50 Gift-card to Troy's Burgers!
   - 1 entry per order

Below you will see whether your our lucky winner
Good luck!!

----------------------------------------------------------------    ''')


def show_winner():
    winner = random.choice(prezzy)
    if winner == 7:
        print(
            "You are a winner!!! Congratulations, you have won our"
            " monthly giveaway of the $50 Troy's burgers Gift-card")
    else:
        print("Unfortunately you not a winner this time, Better luck next time!")

    print()


def show_sides():
    print('''\n
----- SIDES -----

Please select the sides you want by typing in the name from the list below:
1. Hot Chips $5 (chips)
2. Onion Rings $6 (rings)

-------------------------------------------------------------------------------''')


# makes it so that you cant leave a blank space resulting in always getting an answer.
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this field cannot be blank. Please try again")
        else:
            return response


def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


def currency(x):
    return "${:.2f}".format(x)


def string_checker(question, num_letters, valid_responses):
    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def calc_burger_price(var_burger):
    price = 0
    if var_burger == "cheese":
        price = 12.5

    elif var_burger == "bacon":
        price = 17.5

    elif var_burger == "chicken":
        price = 15

    elif var_burger == "vegan":
        price = 14
    return price


# main routine starts

# max amount of burgers you can purchase in one order and the starting amount of burgers before the order.
MAX_BURGERS = 10
burgers_sold = 0

# Main routine starts here

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
burger_list = ["cheese", "bacon", "chicken", "vegan"]
size_list = ["double", "single"]
side_list = ["chips", "rings", "xxx"]
prezzy = [1, 2, 3, 4, 5, 6, 7, 8]

# dictionaries to hold all the burger details
all_burgers = []
all_sides = []
BURGERS_SOLD_LIST = []
PRICES_LIST = []
SIDE_PICKED = []

mini_movie_dict = {
    "Burger": all_burgers,
    "Side Price": all_sides
}

another = "yes"
print("Welcome to Troy's Big Burgers!")
input_name = not_blank("Please enter the name you would like your order under:")
name = capitalize_name(input_name)
phone = num_check("Please enter a contact number so we can let you know if we have any issues:")

while another == "yes":

    want_instructions = string_checker("Do you want to read the "
                                       "instructions and menu {}? (y/n): ".format(name),
                                       1, yes_no_list)
    # if the user wants to view the instructions and says yes this
    # will display the instructions using the show_instructions() command
    if want_instructions == "yes":
        show_instructions()

    print()

    print("Please remember to be to use the word in the bracket, e.g. \"(cheese)\" ")
    which_burger = string_checker("Which burger do you want: ", 1, burger_list)
    if which_burger == "Cheese":
        print()
        print("You selected the Classic Cheese Burger")
        pass
    elif which_burger == "Bacon":
        print()
        print("You selected the Big Bacon Burger")
        pass
    elif which_burger == "Chicken":
        print()
        print("You selected a Cheesy Chicken Burger")
        pass
    elif which_burger == "Vegan":
        print()
        print("You selected a Exquisite Vegan Burger")
        pass
    burger_cost = calc_burger_price(which_burger)

    print()
    size_choice = string_checker("Please choose from single or double protein(+$4): ", 1, size_list)

    if size_choice == "single":
        # size_scale == "S"
        size = 0
        print()
        print("You have selected single protein for your {} burger (no additional cost!)".format(which_burger))
    elif size_choice == "double":
        # size_scale == "L"
        size = 4
        print()
        print("You have selected double protein for your {} burger ($4 dollars more)".format(which_burger))
    else:
        size = 0

    burger_cost = burger_cost + size
    which_sides = 'none'
    temp_sides = []

    want_sides = string_checker("Would you like sides with your burger? (y/n): ",
                                1, yes_no_list)
    if want_sides == "yes":
        show_sides()
        while which_sides != 'xxx':
            which_sides = string_checker("Which Sides would you like (type in \'xxx\' to quit): ",
                                         1, side_list)
            if which_sides == "chips":
                print()
                print("You selected Hot Chips as a side")
                burger_cost = burger_cost + 5
                temp_sides.append(which_sides)
                pass
            elif which_sides == "rings":
                print()
                print("You selected Onion Rings as a side")
                burger_cost = burger_cost + 7.5
                temp_sides.append(which_sides)
                pass

            elif which_sides == 'xxx':
                if len(temp_sides) > 0:
                    print()
                    print("All of your sides have been added!")
                else:
                    print("No Sides will be added then!")
                    temp_sides.append("None")
    else:
        print()
        print("No Sides will be added then!")
        temp_sides.append("None")
        pass

    temp_list = []
    print()
    # an order summary following each burger and sides order you want,
    # it will then prompt the user if they want to add another burger to their order.
    print("------------------------------------------------------------------------")
    print("You ordered a {} {} Burger the Sides of {} for a final cost ${:.2f}".format(size_choice, which_burger,
                                                                                       temp_sides, burger_cost).replace(
        '[', '').replace(']', '').replace('\'', ''), )

    temp_list.append(size_choice)
    temp_list.append(which_burger)
    BURGERS_SOLD_LIST.append(temp_list)
    PRICES_LIST.append(burger_cost)
    SIDE_PICKED.append(temp_sides)

    print()
    another = string_checker("Would you like to order another burger? ",
                             1, yes_no_list)
    if another == "no":
        break
print()
print("You selected a total of {} burgers".format(len(PRICES_LIST)))
print("This comes to a total cost of ${:.2f}".format(sum(PRICES_LIST)))
print()
print("***** Order Summary *****")
print("{}'s Order:               ".format(name))
print("Thanks for ordering with us {}, you're final order is:".format(name))
# places the end users chosen burger,sides, and the total price in one order,
# using .replace is used to take away all spare brackets to blank which makes it nicer.
print("A {} burger with {} as the sides with a total cost of ${}".format(BURGERS_SOLD_LIST, SIDE_PICKED,
                                                                         sum(PRICES_LIST), ).replace('[', '').replace(
    ']', '').replace('\'', ''), )

print()
print("******PAYMENT CHOICE******")
which_pay = string_checker("Would you like to pay in cash or credit (%3 fee): ", 1, payment_list)

if which_pay == "cash":
    print("Paying with cash. Your final cost remains at ${:.2f} ".format(sum(PRICES_LIST)))
elif which_pay == "credit":
    final_cost = sum(PRICES_LIST) * 1.03
    print("Paying with credit. Your final cost is ${:.2f}".format(final_cost))

print()

want_prize = string_checker("Would you like to enter our monthly giveaway?"
                            " (y/n): ",
                            1, yes_no_list)
if want_prize == "yes":
    show_prize()
    show_winner()

print("Thank you for ordering from us {}, Your order will be ready in 10-15 Minutes,"
      " We will contact you on this number ({}) if there is any issues.".format(name, phone))
