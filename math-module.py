import math
import random

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(round(4.5))  # 4 because of even number
print(round(5.5))  # 6 because of odd number
print(math.log(100, 5))


print(random.randint(0, 20))

my_list = list(range(20))
print(random.choice(my_list))

# sample with replacement

print(random.choices(population=my_list, k=10))

# sample without replacement

print(random.sample(population=my_list, k=10))

random.shuffle(my_list)
print(my_list)
