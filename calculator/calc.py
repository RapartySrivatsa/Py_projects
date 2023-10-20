# Basic calculator program
operator = input("Enter an operator (+ - * / %): ")

if operator == "+":
    num1 = float(input("Enter a num1: "))
    num2 = float(input("Enter a num2: "))
    result = num1 + num2
    print(round(result, 2))

elif operator == "-":
    num1 = float(input("Enter a num1: "))
    num2 = float(input("Enter a num2: "))
    result = num1 - num2
    print(round(result, 2))

elif operator == "*":
    num1 = float(input("Enter a num1: "))
    num2 = float(input("Enter a num2: "))
    result = num1 * num2
    print(round(result, 2))

elif operator == "/":
    num1 = float(input("Enter a num1: "))
    num2 = float(input("Enter a num2: "))
    result = num1 / num2
    print(round(result, 2))

elif operator == "%":
    num1 = float(input("Enter a num1: "))
    num2 = float(input("Enter a num2: "))
    result = num1 % num2
    print(round(result, 2))

else:
    print(f"{operator} invalid operator! Enter again")
