def display_board(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = ["  ", "  ", "  "]
row2 = ["  ", " X ", "  "]
row3 = ["  ", "  ", "  "]
display_board(row1, row2, row3)


def user_choice():
    choice = "WRONG"
    within_range = False
    while (choice.isdigit() == False) or (within_range == False):
        choice = input("Please enter a number (0-10)")

        if choice.isdigit():
            if int(choice) in range(0, 10):
                within_range = True

    return int(choice)


user_choice()
