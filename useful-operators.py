from random import shuffle
from random import randint
# range operator range(start, limit, skip)
# limit not included

# for num in range(10):
#     print(num)

# for num in range(3, 10):
#     print(num)

for num in range(0, 10, 2):
    print(num)

my_list = list(range(0, 10, 2))
print(my_list)

# enumerate operator

word = "abcde"
for (index, letter) in enumerate(word):
    print(word[index])

# zip function zip together
# the shortest list

my_list_two = [1, 2, 3, 4]
my_list_three = ["a", "b", "c"]
my_list_four = [100, 200, 300, 400, 500]
for item in zip(my_list_two, my_list_three):
    print(item)

print(list(zip(my_list_two, my_list_three)))


# in keyword

print("x" in [1, 2, 3])
print(1 in [2, 4, 1])
print("a" in "subha")
print("k1" in {"k1": 1, "k2": 2})
print(1 in {"k1": 1, "k2": 2}.values())


# min and max

number_list = [1, 2, 3, 44, 100, -22]
print(min(number_list))
print(max(number_list))


dummy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(dummy_list)
print(dummy_list)

print(randint(0, 20))

response = input("Type a number")
print(f"you typed number {response}")
print(type(response))
