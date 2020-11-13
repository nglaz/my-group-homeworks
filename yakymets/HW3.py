with open('users.txt', 'r+', encoding='utf-8') as f:
    question = input(
        'Проходили ли Вы регистрацию на нашем ресурсе? [да], [нет]\n').lower()
    if question == 'да':
        login = input('Введите Ваш логин\n')
        x = f.read().split()
        if login in x:
            password = input('Введите Ваш пароль ')
            if password in x:
                words = "Вы успешно вошли в систему"
                print(words)
            else:
                words2 = "ошибка"
                print(words2)
        else:
            print('ошибка ')
    elif question == 'нет':
            question = input(
                'Хотели бы Вы зарегистрироваться ?[да],[нет]\n').lower()
            if question == 'да':
                with open('users.txt', 'a+', encoding='utf-8') as f:
                    login = input('Введите Ваш новый логин')
                    password = input('Введите Ваш новый пароль')
                    f.write(f'{login} {password}\n')
                    print('Поздравляю с регистрацией')
            else:
                print('Хорошего Вам дня')
