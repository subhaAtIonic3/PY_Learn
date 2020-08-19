def crate_cubes(n):
    # result = []
    for x in range(n):
        # result.append(x**3)
        yield x**3
    # return result


<<<<<<< HEAD
# for x in crate_cubes(10):
#     print(x)


def print_fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        (a, b) = (b, a+b)


# for x in print_fib(8):
#     print(x)


def simple_gen():
    for x in range(3):
        yield x


for num in simple_gen():
    print(num)

g = simple_gen()
print(g)
print(next(g))
print(next(g))


s = "hello"
iter_str = iter(s)
print(next(iter_str))
print(next(iter(iter_str)))
=======
for x in crate_cubes(10):
    print(x)
>>>>>>> 46012aa7e5c08036f2bf6666eb093b619a1b6bc0
