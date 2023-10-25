# down countdown timer
import time

my_time = int(input("Enter the time in sec: "))

for x in reversed(range(1, my_time + 1)):
    seconds = x % 60  # limit upto 60 counts
    minutes = int(x / 60) % 60  # conv to mins
    hours = int(x / 3600)  # %24 excl as no days in countdown

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
