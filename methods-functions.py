from random import shuffle

my_list = list(range(1, 4))
print(my_list)
my_list.append(4)
my_list.pop()

my_list.insert(2, 90)
print(my_list)


def welcome_user(user_name="default"):
    return(f"Wlcome {user_name}!")


print(welcome_user("Subha"))

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(list_data):
    even_list = []
    for number in list_data:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list


print(is_even(list_data))

work_list = [("a", 200), ("b", 400), ("c", 500), ("d", 100)]


def work_most(work_list):
    max_hrs = 0
    emp_name = ""
    for name, hrs in work_list:
        if hrs > max_hrs:
            max_hrs = hrs
            emp_name = name
    print(f"{emp_name} is the employee of the year with {max_hrs}")


work_most(work_list)

# Game -1

initial_list = ["", "O", ""]
shuffle(initial_list)


def player_guess():
    guess = ""
    while guess not in ["0", "1", "2"]:
        guess = input("Pick a number between 0,1 or 2")
    return int(guess)


def check_guess(shuffle_list, guess):
    print(guess)
    if shuffle_list[guess] == "O":
        print("Correct!")
    else:
        print("Wrong!")
        print(shuffle_list)


shuffle_list = initial_list
check_guess(shuffle_list, player_guess())
