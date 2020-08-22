import time
import timeit


def func_list(n):
    return [str(num) for num in range(n)]


start_time = time.time()
func_list(1000000)
print("dif one => ", (time.time() - start_time))


def func_list_two(n):
    return list(map(str, range(n)))


start_time = time.time()
func_list_two(1000000)
print("dif two => ", (time.time() - start_time))

stmt = '''
func_list(100)
'''

setup = '''
def func_list(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=100000))


stmt2 = '''
func_list_two(100)
'''

setup2 = '''
def func_list_two(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=100000))
