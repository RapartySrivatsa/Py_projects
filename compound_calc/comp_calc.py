# compund interest calculator
pple = 0
rate = 0
time = 0

while True:
    pple = float(input("Enter the principle amount: "))
    if pple < 0:
        print("pple can only be higher than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("rate can only be higher than 0")
    else:
        break

while True:
    time = int(input("Enter the time in year/s: "))
    if time < 0:
        print("time can only be higher than 0")
    else:
        break

total = pple * pow(1 + (rate / 100), time)
print(f"The compound interest after {time} year will be ${total:.2f}")
