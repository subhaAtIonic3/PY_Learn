def func_main(choice=1):
    print("This is func_main()")

    def func_one():
        print("\t This is func_one() inside func_main")

    def func_two():
        print("\t This is func_two() inside func_main")

    print("return a function")

    if choice == 1:
        return func_one
    else:
        return func_two


# one = func_main(choice=1)
# two = func_main(choice=2)

# one()

def hello():
    return "Hi Subha"


def other(some_def_func):
    print("Inside other")
    print(some_def_func())


# other(hello)


def new_decorator(original_func):
    def wrapped_func():
        print("<<== Before ==>>")
        original_func()
        print("<<== After ==>>")

    return wrapped_func


# def func_need_decorator():
#     print("needs to be decorated")


# decorated_func = new_decorator(func_need_decorator)

# decorated_func()

@new_decorator
def func_need_decorator():
    print("needs to be decorated")


func_need_decorator()
