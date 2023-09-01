def calc_burger_price(var_burger):
    price = 0
    if var_burger == "cheese":
        price = 12.5

    elif var_burger == "bacon":
        price = 17.5

    elif var_burger == "chicken":
        price = 15


    return price
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)



burger_list = ["cheese", "bacon", "chicken"]

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

burger_cost = calc_burger_price(which_burger)

print("You ordered a {} Burger the Sides of  for a final cost ${:.2f}".format(which_burger,
                                                                                     burger_cost))