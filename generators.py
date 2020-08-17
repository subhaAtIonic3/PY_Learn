def crate_cubes(n):
    # result = []
    for x in range(n):
        # result.append(x**3)
        yield x**3
    # return result


for x in crate_cubes(10):
    print(x)
