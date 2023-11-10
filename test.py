# calculator
# adventure game
# quizz game
import random

capLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]
specal_letter = ["~", "!", "@", "#", "$", '%', '^', '&', '*', '(', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}',
                 ';', ':', "'", "<", ">", '>', ".", '/', "?", '"']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
check = specal_letter + capLetters


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


# password_gen()


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
