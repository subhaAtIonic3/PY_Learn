
import datetime


my_time = datetime.time(15, 41)
print(my_time)

today = datetime.date.today()
print(today)
print(today.ctime())

my_datetime = datetime.datetime(2021, 8, 19, 16, 5, 1)
print(my_datetime)
my_datetime = my_datetime.replace(year=2020)
print(my_datetime)

day = datetime.date(2020, 8, 5)

d1 = datetime.datetime(2021, 8, 5, 16, 5, 1)
d2 = datetime.datetime(2020, 8, 5, 15, 5, 1)

time_delta = d1 - d2

print(f"equivalent seconds for days => {time_delta.total_seconds()} seconds")
print(f"difference days => {time_delta.days} days")
print(f"difference time => {time_delta.seconds} seconds")
print("Now => ", datetime.datetime.now())
