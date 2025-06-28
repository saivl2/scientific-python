user_name = input('Username: ')
password = input("Password: ")

password_length = len(password)

print(f"{user_name}, your password {'*' * password_length} is {password_length} letters long.")