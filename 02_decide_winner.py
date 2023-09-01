import random

def show_winner():
    winner = random.choice(prezzy)
    if winner == 7:
        print("You are a winner!!! Congratulations, you have won our monthly giveaway of the $50 Troy's burgers Giftcard")
    else:
        print("Unfortunately you not a winner this time, Better luck next time!")

    print()

def string_checker(question, num_letters, valid_responses):

        error = "Please choose a valid input"

        while True:
            response = input(question).lower()

            for item in valid_responses:
                if response == item[:num_letters] or response == item:
                    return item

            print(error)

yes_no_list = ["yes", "no"]
prezzy = [1, 2, 3, 4, 5, 6, 7, 8]
want_prize = string_checker("Would you like to enter our monthly giveaway?"
                            " (y/n): ",
                            1, yes_no_list)
if want_prize == "yes":

    show_winner()