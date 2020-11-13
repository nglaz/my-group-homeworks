login_in = input(
    'Are you registered? (Press enter \'YES\' or \'NO\')').upper()
if login_in == 'YES':
    with open('users.txt') as file:
        users = file.read().split()
        login_user = input('Your login:')
    if login_user in users:
        pass_user = input('Your password:')
        if users[users.index(login_user) + 1] == pass_user:
            print('Your welcome in our system!')
        else:
            print('Your password is not correct, please check')
    else:
        print('Your login is not correct, please check')
else:
    register_in = input(
    'Would you like to register now?(Press enter \'YES\' or \'NO\')').upper()
    if register_in == 'YES':
        login_user = input('Please enter your login:')
        pass_user = input('Please enter your password:')
        registr_f = open('users.txt', 'a+')
        registr_f.write('\n' + login_user + '\n' + pass_user)
        print('You successful registration')
    else:
        print('Have a nice day')
