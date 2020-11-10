# my-group-homeworks
with open('users.txt', 'r+', encoding='utf-8') as f:
    word = input('Здравствуйте, вы проходили регистрацию на нашем ресурсе? [Да], [Нет]\n').lower()
    if word == 'да':
        login = input('Введите логин от вашего аккаунта')
        text = f.read().split()
        if login in text:
            password = input('Введите пароль от вашего аккаунта')
            if password in text:
                print('Вход в аккаунт успешно осуществлён')
            else:
                print('Ошибка при входе')
        else:
            print('Ошибка при входе')
    elif word == 'нет':
        word = input('Вы желаете зарегестрироваться на нашем портале? [Да], [Нет]\n').lower()
        if word == 'да':
            with open('users.txt', 'a+', encoding='utf-8') as f:
                login = input('Введите желаемый логин вашего аккаунта')
                password = input('Введите желаемый пароль вашего аккаунта')
                f.writelines(login + ' ' + password + '\n')
            print('Регистрация прошла успешно')
        else:
            print('Желаю вам хорошего дня')
