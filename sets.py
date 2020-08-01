#  unordered collection of unique elements
my_set = set()

my_set.add(1)
my_set.add(2)

print(my_set)

# nothing happen
my_set.add(2)
print(my_set)

my_list = [1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2]
print(set(my_list))
