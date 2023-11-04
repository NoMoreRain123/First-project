import random

global guest_bill
global split_bill


def rock_paper_scisssors():
    choices = "Rock", "Paper", "Scissors"
    rock, paper, scissors = choices
    pc_throw = random.choice(choices)
    winner = 0
    pc_win = winner == 2
    player_win = winner == 1
    tie = winner == 3
    win_loss_count = 0

    print("so you think your good a Rock Paper Scissors??")
    print("Lets test your skills then")
    you_throw = input()
    if you_throw == rock and pc_throw == scissors:
        winner = 1
    elif you_throw == pc_throw:
        winner = 3
    elif you_throw == rock and pc_throw == paper:
        winner = 2
    elif you_throw == paper and pc_throw == rock:
        winner = 1
    elif you_throw == paper and pc_throw == scissors:
        winner = 3
    elif you_throw == scissors and pc_throw == rock:
        winner = 3
    elif you_throw == scissors and pc_throw == paper:
        winner = 2
    if winner == 1:
        print("Well not bad you can try again sense we tied")
        rock_paper_scisssors()
    elif winner == 2:
        print("Well you did it you can play again or you can Take your win and leave")
        print("to play again type 1 or presss 2 to return to start")
        after_game = input()
        if after_game == "1":
            rock_paper_scisssors()
        else:
            start()
    elif winner == 3:
        print("Just as I expected YOU LOST but you can try again or cut you losses.")
        print("if you wish")
        print("to play again type 1 or presss 2 to return to start")
        after_game = input()
        if after_game == "1":
            rock_paper_scisssors()
        else:
            start()
    else:
        print("But Why wouldn't you want to play a game hmm...")
        input()
        start()


def tip_genorator():
    print("How much was the bill.")
    guest_bill = input()
    while True:
        try:
            guest_bill = float(guest_bill)
            break
        except ValueError:
            print("only numbers")
            tip_genorator()
    print("Will you be splitting the bill tonignt(Yes or No)")
    split_bill_answer = input()

    if split_bill_answer != "Yes":
        print("how much Would you like to tip?")

        tip_percent = input()
        while True:
            try:
                tip_percent = float(tip_percent)
                print("Your total is")
                tip_percent = tip_percent / 100
                total = (tip_percent * guest_bill) + guest_bill
                print(total)
                break
            except ValueError:
                print("only numbers")
                tip_genorator()
    else:
        print("How many ways will we be splitting the bill?")
        split_bill = input()
        while True:
            try:
                split_bill = float(split_bill)
                bill = guest_bill / split_bill
                print("how much Would you like to tip?")
                tip_percent = input()
                while True:
                    try:
                        tip_percent = float(tip_percent)
                        break
                    except ValueError:
                        print("only numbers")
                        tip_genorator()
                print("Your total is")
                tip_percent = tip_percent / 100
                total = (tip_percent * bill) + bill
                print(total)
                break
            except ValueError:
                print("only numbers")
                tip_genorator()

    quit()


def number_guessing():
    arange = range(1, 10)
    attempt = 0
    answer = int(random.choice(arange))
    print("This is the NGG(number guessing game).")
    print("Its quite simple you know. All you must do is guess the right number for a given range.")
    print("There will be multiple rounds for each round you will type the letter you think it is.")
    print("You will get a few hints each time you make a mistake. But not ALWAYS.")
    print("Lets start easy")
    # Change game range and hints and add more rounds.
    guess = " "
    print("Alright Guess a number 1-3")
    while guess != answer:
        attempt = attempt + 1
        guess = input(int())
        if answer == (guess):
            print('Correct')
            break
        elif attempt == 2:
            if answer <= 5:
                print("(Hint) The Answer is 5 or less")
            else:
                print("(Hint) The Answer is More Then 5")
        elif attempt == 1:
            if answer % 2 == 0:
                print("Wrong\n(hint) The number is even")
        elif attempt == 1:
            print('Wrong\n(hint)The number is odd')


def start():
    print("What would you like to do")
    print("You Have An Assortment of options Type the number and press enter of the one you wish to play.")
    print("Press enter to quit.")
    print('0. Number Guessing Game 1. Rock Paper Scissors', "\n2. Tip Genorator", "3. Calculator")
    choice_list = [number_guessing, rock_paper_scisssors, tip_genorator]
    choice_index = input()
    choice_index = int(choice_index)
    choice_list[choice_index]()


start()
