# Credit card validator program

sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1: Remove all '-' and ' '
card_number = input("Enter a credit card no: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")

# Step 2: Add all the odd place digits from right to left
card_number = card_number[::-1]  # reverse digits
for x in card_number[::2]:
    sum_odd_digits += int(x)

# Step 3: Double digits from right to left
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += 1 + (x % 10)
    else:
        sum_even_digits += x

# step 4: Add odd + even digits
total = sum_even_digits + sum_odd_digits

# step 5: Total % 10 == 0 then valid card
if total % 10 == 0:
    print("Valid Card")
else:
    print("Invalid Card, Please Recheck!")
