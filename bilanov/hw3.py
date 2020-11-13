a = input('Zdravstvuyte, Vi uzhe zaregistrirovani na nashem resurse? '
          'Esli da, vvedite "Yes", esli net vvedite "No".\n')
f = open('users.txt', 'a+', encoding='utf-8')
f.seek(0)
users = f.read().split()

if a == 'Yes':
    login = input('Vvedite svoi login: ')

    if login in users:
        print('Login naiden!')
        password = input('Vvedite svoi parol: ')
        if password in users:
            if users.index(login) == users.index(password) - 1:
                print('Vhod uspeshen!')
            else:
                print('Neverniy parol!')
        else:
            print('Neverniy parol!')
    else:
        print('Login ne naiden(')
elif a == 'No':
    b = input('Vi zhelaete zaregistrirovatsa na nashem resurse? '
              'Vvedite "Yes" or "No".\n')
    if b == 'Yes':
        login1 = input('Pridumayte login: ')
        password1 = input('Pridumayte parol: ')
        f.write('\n' + login1 + '\n' + password1)
        print('Dobro pozhalovat na nash resurs!')
    elif b == 'No':
        print('nu i ladno(')
f.close()
