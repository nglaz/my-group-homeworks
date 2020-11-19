test = input('проходили ли вы регистрацыю: ')
if test == 'да':
    name_f = input('введи имя пользователя: ')
    password_f = input('введи пароль: ')
    with open('name_password', 'r+') as f1:
        np = f1.read()
        if name_f in np and password_f in np:
            print('вход успешен')
        else:
            print('вы не зарегестрированы')
else:
    question = input('хотите пройти регистрацыю: ')
    if question == 'да':
        name = input('введи имя пользователя: ')
        password = input('введи пароль: ')
        password_test = int(input('введи пароль повторно: '))
        with open('name_password', 'a') as f:
            f.write(name)
            f.write('\n'+password)
    else:
        print('удачи')