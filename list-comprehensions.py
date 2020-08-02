my_string = "hello"
my_list = []

for letter in my_string:
    my_list.append(letter)
print(my_list)

my_list_two = []
my_list_two = [item for item in "World"]
print(my_list_two)

my_number_list = [num**2 for num in range(0, 20, 2)]
print(my_number_list)

even_list = [num for num in range(0, 11) if num % 2 == 0]
print(even_list)

celsius = [0, 10, 20, 32.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)


# Not recommended
result = [num if num % 2 == 0 else "ODD" for num in range(0, 11)]
print(result)


my_nested_list = []

for x in [1, 2, 3]:
    for y in [1, 10, 1000]:
        my_nested_list.append(x*y)
print(my_nested_list)

my_nested_list = [x*y for x in [1, 2, 3] for y in [1, 10, 1000]]
print(my_nested_list)
