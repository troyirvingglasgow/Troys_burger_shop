def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


size_list = ["double", "single"]
burger_list = ["cheese", "bacon", "chicken"]
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

size_choice = string_checker("Please choose from single or double protien(+$4): ", 1, size_list)

if size_choice == "single":
        # size_scale == "S"
        size = 0
        print()
        print("You have selected single protien for your burger(no additional cost!)".format(which_burger))
elif size_choice == "double":
        # size_scale == "L"
        size = 4
        print()
        print("You have selected double protien for your burger ($4 dollars more)".format(which_burger))
else:
        size = 0