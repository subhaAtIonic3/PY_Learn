my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in my_list:
    if item % 2 == 0:
        print("Even =>", item)
    else:
        print("Odd =>", item)

sum = 0
for item in my_list:
    sum += item

print(f"Sum is {sum}")

for _ in "SUBHA":
    print("HI")

my_tup = (1, 2, 3)
for item in my_tup:
    print(item)

# Tuple unpacking
new_list = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for (a, b) in new_list:
    print(a)
    print(b)

my_dict = {"k1": 1, "k2": 2, "k3": 3}
for (key, value) in my_dict.items():
    print(f"Dictionaries values are => {value}")

dummy_list = [1, 2, 3]
for item in dummy_list:
    pass
print("EOS")

name = "SUBHA"
for letter in name:
    if letter == "S":
        continue
    else:
        print(f"Letter => {letter}")

name_two = "XOLO"
for letter in name_two:
    if letter == "L":
        break
    else:
        print(f"letter => {letter}")
print(f"Print name_two here {name_two}")
