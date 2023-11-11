import random
global guest_bill
global split_bill


def rock_paper_scisssors():
    choices = "Rock", "Paper", "Scissors"
    rock, paper, scissors = choices
    pc_throw = random.choice(choices)
    winner = 0

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
        if answer == guess:
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
def todolist():
    todo_list = []
    print("This is a todo list.")
    print("What should be first")
    todo_list_add = input("Add New Todo\n")
    todo_list.append(todo_list_add)
    print("Would you like to add another thing to do or\nsee all your todos ")
    while True:
        next_choice = input("Type Home to see all todos.\nType New to add something else")
        if next_choice == "Home":
            print(todo_list)
            break
        else:
            todo_list_add = input("Add New Todo\n")
            todo_list.append(todo_list_add)

# calculator
# adventure game
# quizz game


capLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]
specal_letter = ["~", "!", "@", "#", "$", '%', '^', '&', '*', '(', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}',
                 ';', ':', "'", "<", ">", '>', ".", '/', "?", '"']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
check = specal_letter + capLetters

def password_help():
    def password_gen():
        your_password = random.sample(check, 25)
        x = "".join(your_password)
        print("your password is")
        print(x)
        choice = input("type New if you would like another or type save to save it to your paswords")
        print("you can also see all the passwords you've saved")
        if choice == "New":
            password_gen()
        elif choice == "new":
            password_gen()
        # add saved
    def password_check():
        cap_letters_check_list = []
        password_lenth_check_list = []
        number_check_list = []
        specal_letters_check_list = []
        password_input = input("Enter Password\n")
        password = list(password_input.strip(""))
        for x in password:
            for y in capLetters:
                if x == y:
                    cap_letters_check_list.append("f")
                    break
            for a in numbers_list:
                if x == a:
                    number_check_list.append("d")
                    break
            for b in specal_letter:
                if x == b:
                    specal_letters_check_list.append("iju")
                    break
        if len(password) > 8:
            password_lenth_check_list.append("9i9i9")
        check_list = [len(cap_letters_check_list), len(password_lenth_check_list), len(number_check_list),
                      len(specal_letters_check_list)]
        if check_list[1] < 1:
            print("Try increasing the lenth of your password")
            password_check()
        elif check_list[2] < 1:
            print("Try adding atleast one number")
            password_check()
        elif check_list[0] < 1:
            print("Try adding at least one capital letter")
            password_check()
        elif check_list[3] < 1:
            print("Try Adding a specal charecter or symbol")
            password_check()
        else:
            print("Password is strong enough")

    print("password strenth checker is .1\npassword genorator is .2\n")
    choice_list = [password_check, password_gen]
    choice_index = input()
    choice_index = int(choice_index)-1
    choice_list[choice_index]()


def start():
    print("What would you like to do")
    print("You Have An Assortment of options Type the number and press enter of the one you wish to play.")
    print("Press enter to quit.")
    print('0. Number Guessing Game 1. Rock Paper Scissors', "\n2. Tip Genorator", "3. todo list", "4. Password Help")
    choice_list = [number_guessing, rock_paper_scisssors, tip_genorator, todolist, password_help]
    choice_index = input()
    choice_index = int(choice_index)
    choice_list[choice_index]()


start()
