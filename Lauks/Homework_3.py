signed_in = input('Already registered? (Type enter \'yes\' or \'no\')').lower()
if signed_in == 'yes':
    users = {}
    with open('users.txt') as file:
        for line in file:
            key, value = line.split()
            users[key] = value
    login = input('Please enter your login')
    if login in users:
        password = input('Please enter your password')
        if users[login] == password:
            print('Login successful')
        else:
            print('Please check your password')
    else:
        print('Please check your login')
elif signed_in == 'no':
    sign_up = input('Would you like to sign up?(Type enter \'yes\' or \'no\')').lower()
    if sign_up == 'yes':
        login = input('Please enter your login')
        password = input('Please enter your password')
        with open('users.txt', 'a') as file:
            file.write('\n' + login)
            file.write(' '+ password)
        print('Registration complete')
    elif sign_up == 'no':
        print('Good luck!')
    else:
        print('Incorrect answer! Please try again.')
else:
    print('Incorrect answer! Please try again.')