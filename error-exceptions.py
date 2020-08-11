try:
    result = 20 + "20"
except:
    print("This is the except block")
else:
    print("Went well, no error")
    print(result)


try:
    f = open("test-file.txt", "r")
    f.write("Write from python")
except TypeError:
    print("There was a type error")
except OSError:
    print("You have an OS error")
finally:
    print("It's always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number => "))
        except:
            print("Wrong! It's not a number")
            continue
        else:
            print("Thanks for the input")
            break
        finally:
            print("End on try/except/finally")


ask_for_int()
