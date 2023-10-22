# email slicing using string indexing method

email = input("please enter your email: ")

# index = email.index("@")

username = email[: email.index("@")]
domain = email[email.index("@") + 1 :]

print(f"Your username is {username}")
print(f"Your domain is {domain}")
