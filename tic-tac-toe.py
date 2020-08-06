row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

user_input_index = list(range(1, 10))

wining_conditions = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]

acceptable_postions = list(range(1, 10))


def check_user_win():
    for i in wining_conditions:
        [a, b, c] = i
        # print([a, b, c])
        if get_user_value(a) == get_user_value(b) == get_user_value(c):
            # print(get_user_value(a))
            # print(get_user_value(b))
            # print(get_user_value(c))
            if get_user_value(a) == False:
                pass
            elif get_user_value(a) == "X":
                display_board()
                print("User one win")
                return True
            else:
                display_board()
                print("User two win")
                return True
    return False


# def check_draw_status(for_row):
#     for value in for_row:
#         if value == " ":
#             return False
#         else:
#             pass
#     return True


def display_board():
    print(row1)
    print(row2)
    print(row3)


def check_winner(is_user_one):
    win_status = check_user_win()
    # print("Check user stats => ", win_status)
    if win_status:
        return
    else:
        # draw_status_at_row1 = check_draw_status(row1)
        # draw_status_at_row2 = check_draw_status(row2)
        # draw_status_at_row3 = check_draw_status(row3)
        # print("row 3 =>", check_draw_status(row3))
        # print("row 2 =>", check_draw_status(row2))
        # print("row 1 =>", check_draw_status(row1))
        # if draw_status_at_row1 == draw_status_at_row2 == draw_status_at_row3:
        #     print("It's a draw!!")
        #     display_board()
        # else:
        display_board()
        user_input(is_user_one)


def get_user_value(postion):
    if postion in [1, 2, 3]:
        user_value = row1[postion - 1]
    elif postion in [4, 5, 6]:
        user_value = row2[postion - 4]
    else:
        user_value = row3[postion - 7]

    return False if user_value == " " else user_value


def display_user_turn(is_user_one):
    if is_user_one:
        print("<= User one place X in the board =>")
    else:
        print("<= User two place O in the board =>")


def user_actual_input_position(row_position, position, is_user_one):

    if len(user_input_index) == 0:
        print("It's a draw!!")
    else:
        if row_position == 1:
            if row1[position] == " ":
                row1[position] = "X" if is_user_one else "O"
                user_input_index.pop()
                check_winner(not is_user_one)
            else:
                print("This place has already been filled")
                display_board()
                user_input(is_user_one)
        elif row_position == 2:
            if row2[position] == " ":
                row2[position] = "X" if is_user_one else "O"
                user_input_index.pop()
                check_winner(not is_user_one)
            else:
                print("This place has already been filled")
                display_board()
                user_input(is_user_one)
        else:
            if row3[position] == " ":
                row3[position] = "X" if is_user_one else "O"
                user_input_index.pop()
                check_winner(not is_user_one)
            else:
                print("This place has already been filled")
                display_board()
                user_input(is_user_one)


def user_input(is_user_one=False):

    display_user_turn(is_user_one)
    user_position = "Wrong"
    in_range = False

    while user_position.isdigit() == False or in_range == False:
        user_position = input("Please inset user position (1-9) => ")

        if user_position.isdigit() == False:
            print("Please use a valid input")

        if user_position.isdigit():
            if int(user_position) in acceptable_postions:
                in_range = True

    user_position = int(user_position)

    if user_position in [1, 2, 3]:
        user_actual_input_position(1, user_position - 1, is_user_one)
    elif user_position in [4, 5, 6]:
        user_actual_input_position(2, user_position - 4, is_user_one)
    else:
        user_actual_input_position(3, user_position - 7, is_user_one)


user_input(True)

# check_user_win()
