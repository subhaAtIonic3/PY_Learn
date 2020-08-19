from collections import Counter, defaultdict, namedtuple

my_list = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]

print(Counter(my_list))

print(Counter("ssswiiwssak"))

letters = "aaaaaabbbbbbbcccccccddddddddd"
c = Counter(letters)

print(c.most_common())
print(c.most_common(2))
print(list(c))


my_dict = {"a": 10}
# print(my_dict["wrong"])  will cause an error
print(my_dict)

my_dict = defaultdict(lambda: 0)

my_dict["a"] = 10

print(my_dict["a"])
print(my_dict["wrong"])
print(my_dict)


Dog = namedtuple("Dog", ["age", "breed", "name"])

coco = Dog(age=4, breed="Lab", name="Coco")

print(coco)
print(type(coco))
print(coco.age)
print(coco.name)
