command: str = input('Are you signed in?\nY - Yes\nN - No\nR - Register\n-').lower()
users = open('users.txt', 'a+')
log = open('log.txt', 'a+')
users.seek(0)
if command == 'y' or command == 'yes':
    login = input('Please log in\nUsername - ')
    password = input('Password - ')
    data = users.read()
    check = 'login: ' + login + ', password: ' + password + '.'
    if check in data:
        print('Welcome back!')
        log.write('user ' + login + ' loged in\n')
    else:
        print('You are not welcome here! *buttle music begins*')
        log.write('user ' + login + ' failed to log in\n')

elif command == 'n' or command == 'no':
    print('Register then!\nOk or not?')
    answer: str = input('What will you chose? - ').lower()
    if answer == 'ok' or answer == 'yes' or answer == 'y':
        print('Then start program again and use "r" or "register" command))))')
    else:
        print('You\'we chosen your destiny. Farewell!')
        log.write('Pure fool doesn\'t know what he\'s just refused\n')

elif command == 'r' or command == 'register':
    login = 'login: ' + input('Chose your login - ')
    password = ', password: ' + input('Password - ') + '.' + '\n'
    users.write(login)
    users.write(password)
    log.write('registered ' + login + '\n')
    print('You are now welcome. Start again and login.')

else:
    print('Please, start again and, input right command.')
    # continue, но это мы еще не учили)

users.close()
log.close()
