with open('users.txt', 'r+', encoding='utf-8') as f:
    question = input('Проходили ли Вы регистрацию на нашем ресурсе? [да], [нет]\n').lower()
    if question == 'да':
        login = input('Введите Ваш логин')
        x = f.read().split()
        if login in x:
            password = input('Введите Ваш пароль ')
            if x[x.index(login)+1] == password :
                print('Вы успешно вошли в систему')
            else:
                print('ошибка')
    elif question == 'нет':
            question = input(
                'Хотели бы Вы зарегистрироваться ?[да],[нет]\n').lower()
            if question == 'да':
                with open('users.txt', 'a+', encoding='utf-8') as f:
                    login = input('Введите Ваш новый логин')
                    password = input('Введите Ваш новый пароль')
                    f.write(login + '\n' + password + '\n')
                print('Поздравляю с регистрацией')
            else:
                print('Хорошего Вам дня')
