# 1. Создать эмуляцию системы входа и регистрации для пользователей
users_base = open("users.txt", "a+")
users_base.seek(0)
polzovatel = users_base.read().split()
# 2. При запуске программы, пользователя должно спросить проходил ли он регистрацию на нашем ресурсе,
loginimsja = input('ti zaregen? ener yes or net').lower()
if loginimsja == 'yes':
    print('napishi login + parol')
# 3. если да, тогда предложить ему ввести логин и пароль от его учетной записи.
    login = input('tvoe imja')
    if login in polzovatel:
        print('ok')
    else:
        print('ne everno')
    password = input('parol')
    users_base.seek(0)
    if password in polzovatel:
        print('ti voshel')
    else:
        print('ne evereno')
# 5. Если пользователь не регистрировался на ресурсе, тогда спросить не желает ли он пройти регистрацию.
elif loginimsja == 'net':
    register = input\
             ('novij login i parol'
# 6. Если желает, взять от него необходимые данные и вывести об успешной регистрации, если не желает
# регистрироватся - пожелать удачи.              
              '(hochesh zaregistrirovatsja ok ili ne)').lower()
    if register == 'ok':
        login = input("login")
        password = input("parol")
# 7. Данные о зарегестрированных пользователях хранить в файле 'users.txt'
        with users_base as file:
            file.write('\n' + login)
            file.write(' ' + password)
        print('ok')
    elif loginimsja == 'ne':
        print('ydachi')
users_base.close()



# 1. Создать эмуляцию системы входа и регистрации для пользователей.
# 2. При запуске программы, пользователя должно спросить проходил ли он регистрацию на нашем ресурсе,
# 3. если да, тогда предложить ему ввести логин и пароль от его учетной записи.
# 4. Если данные верны вывести сообщение об успешном входе в систему, если нет тогда сообщить об это.
# 5. Если пользователь не регистрировался на ресурсе, тогда спросить не желает ли он пройти регистрацию.
# 6. Если желает, взять от него необходимые данные и вывести об успешной регистрации, если не желает
# регистрироватся - пожелать удачи.
# 7. Данные о зарегестрированных пользователях хранить в файле 'users.txt', по желанию можете создать
# файл для логирования событий регистрации и входа.
