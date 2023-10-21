# Exercise on str methods
# Len should be not greater than 12
# username should not have any spaces
# username should only have alphabets

username = input("Enter a username: ")

if len(username) > 12:
    print(f"{username} should not have more than 12 chars!")
elif not username.find(" ") == -1:
    print(f"{username} should not have spaces!")
elif not username.isalpha():
    print(f"{username} cant contain numbers")
else:
    print(f"{username}'s a valid one!")
