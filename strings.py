print("hello \n world")
print("hello \nworld")
print("hello \t world")

print(len("Check length"))

my_string = "Hello World"
print(my_string[9])  # fwd index position
print(my_string[-2])  # bwd index postion

# print(my_string[2:])
# print(my_string[:5])
print("Slice String =>", my_string[2: 9])

print("Step size =>", my_string[::2])
print("Combine Step Size =>", my_string[1:9:3])
print("Reverse a string => ", my_string[::-1])

name = "Subha"
print("p" + name[1:])

letter = "z"
print(letter * 10)

#  Not possible in python
# letter_two = "2"
# number = 23
# print(letter_two + number)

dummy_string = "Hello"
print(dummy_string.upper(), dummy_string.lower())
print("Split =>", "test string".split())

# String pallindrom
new_string = "maddam"
isPallindrom = (new_string == new_string[::-1])
print("Pallindrom result =>", isPallindrom)


# Advanced String


word = "Hello world!"

print("'o' count in 'Hello world!' is  => ", word.count('o'))
print("first postion of 'o' is => ", word.find('o'))
print("any spacing => ", word.isspace())
print("is alphabetic =>", word.isalpha())
print("is alphanumeric =>", word.isalnum())
print(word.split("o"))
print(word.partition("o"))
print(word.endswith("!"))
