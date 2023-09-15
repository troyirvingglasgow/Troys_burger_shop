def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

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


yes_no_list = ["yes", "no"]
another = string_checker("Would you like to order another burger? ",
                         1, yes_no_list)

while another == "yes":
    show_instructions()
    print()

if another == "no":
    pass
