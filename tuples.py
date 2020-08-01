t = ("s", "u", "b")
print(t, type(t))
list = ["s", "u", "b"]
print(len(t))

print(t[1:])
print("reverse tuples => ", t[::-1])

t_two = (1, 1, 2)
print(t_two)
print("count of 1 =>", t_two.count(1))
print("First index of 1 =>", t_two.index(1))

# Tuples didn't have object assignment
# error t_two[0] = 4
