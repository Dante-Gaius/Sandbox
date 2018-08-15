"""Dante Gaius"""

password = input("Enter password: ")

while len(password) < 6:
    print("Invalid password")
    password = input("Enter password: ")

for char in password:
    print("*", end="")
