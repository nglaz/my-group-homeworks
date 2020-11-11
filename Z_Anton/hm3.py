log = open('log.txt', 'a+')
test = input('проходили ли вы регистрацию ?: ')
if test == 'да':
    with open('users.txt', 'r+') as f1:
        name_f = input('введи имя аккаунта: ')
        password_f = input('введи пароль: ')
        np = f1.read()
        check = 'Your login: ' + name_f + ' your password: ' + password_f
        if check in np:
            print('вход успешен, удачки:)')
        else:
            print('вы не зарегестрированы:(')
else:
    question = input('хотите пройти регистрацыю: ')
    if question == 'да':
        with open('users.txt', 'a') as f:
            name = 'Your login: ' + input('Введи имя аккаунта - ')
            password = ' your password: ' + input('и пароль не забудь) - ') + '\n'
            f.write(name)
            f.write(password)
            log.write('registered: '+name)
    else:
        print('удачи:)')
