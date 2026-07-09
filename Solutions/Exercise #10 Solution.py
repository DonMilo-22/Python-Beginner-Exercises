password = ""

password = input("Enter a password: ")

if len(password) >= 8:
    print("Password accepted.")
else:
    print("Password too short.")
