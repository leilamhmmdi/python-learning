# User Registration
users = []

for i in range(1, 6):
    user = {}

    user['national_code'] = input(f'Enter national code for user {i}: ')
    user['username'] = input(f'Enter username for user {i}: ')
    user['password'] = input(f'Enter password for user {i}: ')

    users.append(user)

print(users)

# Login

national_code = input('Enter national code: ')
username = input('Enter username: ')
password = input('Enter password: ')

found = False

for user in users:
    if (
        user['national_code'] == national_code
        and user['username'] == username
        and user['password'] == password
    ):
        found = True
        break

if found:
    print("Welcome")
else:
    print("Invalid information")
