game_list = ["", "", ""]


def display_game_list():
    print(f"Here is the list {game_list}")


def user_choice():
    choice = "WRONG"
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please pick a postion between (0-2) ")

        if choice.isdigit():
            if (int(choice) in range(0, 3)):
                within_range = True

    return int(choice)


def insert_word():
    choice = user_choice()
    print("Your insert position is =>", choice)
    user_input = ""
    while len(user_input) == 0:
        if game_list[choice] == "":
            user_input = input("Please enter your item => ")
        else:
            user_input = input("Edit your item => ")

    game_list[choice] = user_input
    continue_game()


def continue_game():
    display_game_list()
    user_input = input("Would you like to continue? Y or N => ")

    if user_input.lower() == "y":
        insert_word()
    elif user_input.lower() == "n":
        print("Please visit again!")
        display_game_list()
    else:
        continue_game()


insert_word()
