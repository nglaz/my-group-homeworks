with open("users.txt", 'r+', encoding='utf-8') as f:
    question = input(
        'Проходили ли Вы регистрацию на нашем ресурсе? [Да], [Нет]\n').lower()
    if question == 'Да':
        login = input('Введите Ваш логин')
        x = f.read().split()
        if login in x:
            password = input('Введите Ваш пароль ')
            if password in x:
                words = "Вы успешно вошли в систему"
                print(words)
            else:
                words2 = "Ошибка"
                print(words2)
        elif question == 'Нет':
            question = input(
                'Хотели бы Вы зарегистрироваться ?[Да],[Нет]\n').lower()
            if question == 'Да':
                with open('users.txt', 'r+', encoding='utf-8') as f:
                    login = input('Введите Ваш новый логин')
                    password = input('Введите Ваш новый пароль')
                    f.writelines(login + ' ' + password + '\n')
                    print('Поздравляю с регистрацией')
            else:
                print('Хорошего Вам дня')
