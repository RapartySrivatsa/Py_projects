# weight converter program (Kg -> pounds) or vice-versa
weight = float(input("Enter your weight: "))
unit = input("Kilo or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight,2)} {unit}.")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight,2)} {unit}.")
else:
    print(f"{unit} is invalid! Pls retype")
