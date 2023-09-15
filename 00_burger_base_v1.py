import pandas
import random
from datetime import date

# show menu
def show_menu():
    print('''\n
***** Troy's Burgers *****

      *****MENU*****
      
         **BEEF**
    Classic Cheese $12.50 (1)
   Big Bacon Burger $17.50 (2)
  
        **CHICKEN**
     Cheesy Chicken $15 (3)
     
         **SIDE**
       Hot Chips $5 (4)
      Onion Rings $6 (5)


For each order, enter...
- The person's name (can't be blank)
- Your selected items (from the menu above)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display your recipt
including the cost of each Burger, and the total cost.

This information will automatically written to a text file.
***************************''')

 # checks user response is not blank
def not_blank(question):

        while True:
            response = input(question)

            if response == "":
                print("Sorry this can't be blank. Please try again")
            else:
                return response

 # checks if input is integer
def num_check(question):

        while True:

            try:
                response = int(input(question))
                return response

            except ValueError:
                print("Please enter an integer.")

def calc_ticket_price(burger_price):

    # ticket is $7.50 for users under 16
    if burger_price < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif burger_price < 65:
        price = 10.5

    else:
        price = 6.5

    return price


# calc burger price function
def calc_burger_price(var_burger):
    # Hawaiian Pizza is $7.00
    if var_burger == "Classic Cheese":
        price = 7

    elif var_burger == "Big Bacon Burger":
        price = 6.5

    elif var_burger == "Cheesy Chicken":
        price = 8

    return price

# calc burger price function
def calc_sides_price(var_sides):
    # Hawaiian Pizza is $7.00
    if var_sides == "Hot Chips":
        price = 7

    elif var_sides == "Onion Rings":
        price = 6.5

    return price

# cash / credit based on list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],
                                            valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

# currency format


def currency(x):
    return "${:.2f}".format(x)

# main routine starts here

# set maximum number of tickets below


MAX_Items = 20
MenuItems_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
burger_list = ["Classic Cheese,Big Bacon Burger,Cheesy Chicken,4,5,6"]

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

want_instructions = string_checker("Would you like to view the "
                                   "Menu (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    show_menu()

print()

# loop to sell tickets
while MenuItems_sold < MAX_Items:
    name = not_blank("Please enter what you would like or 'xxx' to quit: ")

    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must buy at least one item off the menu before quitting")
        continue
    order = num_check("What would you like?")

    if order <= 1:
       print("1x Classic Cheese")

    elif order <= 2:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again!")
        continue




mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# calculate total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency format
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

mini_movie_frame = mini_movie_frame.set_index('Name')

# get today's date
today = date.today()

# get day month and year individual
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- Burger ({}/{}/{}) -----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# change frame to string so we can export
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create strings for printing...
ticket_cost_heading = "\n---- Ticket Cost / Profit -----"
total_ticket_sales = "Total Ticket Sales: ${:.2f}".format(total)
total_profit = "Totals Profit: ${:.2f}".format(profit)

# edit text below!! It needs to work if we have unsold tickets
sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${:.2f}. ie: Their ticket is " \
              "free!".format(winner_name, total_won)

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()

# Output number of tickets
if MenuItems_sold == MAX_Items:
    print("You have reached the max amount of food you can have for this order")
else:
    print("You have order {} item/s from our. You have upto {} item/s"
          "remaining".format(MenuItems_sold, MAX_Items- MenuItems_sold))


