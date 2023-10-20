# temp converter
temp = float(input("Enter the temperatur: "))
unit = input("Is it Celsius, Kelvin or Fahrenheit (C, K or F): ")
unit = unit.upper()

if unit == "C":
    temp1 = temp + 273.15
    temp2 = temp * (9 / 5) + 32
    unit1 = "K"
    unit2 = "F"
    print(f"Temp in K and F is:{round(temp1,2)}{unit1} & {round(temp2,2)}{unit2}.")

elif unit == "K":
    temp1 = temp - 273.15
    temp2 = (temp - 273.15) * (9 / 5) + 32
    unit1 = "C"
    unit2 = "F"
    print(f"Temp in C and F is:{round(temp1,2)}{unit1} & {round(temp2,2)}{unit2}.")

elif unit == "F":
    temp1 = (temp - 32) * (5 / 9)
    temp2 = (temp - 32) * (5 / 9) + 273.15
    unit1 = "C"
    unit2 = "K"
    print(f"Temp in C and K is:{round(temp1,2)}{unit1} & {round(temp2,2)}{unit2}.")

else:
    print(f"{unit} is invalid! Pls retype")
