a = input('Zdravstvuyte, Vi uzhe zaregistrirovani na nashem resurse? Esli da, vvedite "Yes", esli net vvedite "No".\n')
f = open('users.txt', 'r+', encoding='utf-8')
proverka = str(f.readlines())
f.seek(0)
if a == 'Yes':
    login = input('Vvedite svoi login: ')
    if login in proverka:
        print('login naiden!')
        f.seek(0)
        password = input('Vvedite svoi parol: ')
        if password in proverka:
            print('Vhod uspeshen!')
            f.seek(0)
        else:
            print('Neverniy parol')
    else:
        print('Dannie dlya vhoda ne verni(')
elif a == 'No':
    b = input('Vi zhelaete zaregistrirovatsa na nashem resurse? Vvedite "Yes" or "No".\n')
    if b == 'Yes':
        login1 = input('Pridumayte login: ')
        password1 = input('Pridumayte parol: ')
        f = open('users.txt', 'a+')
        f.write('\r' + login1 + ' ' + password1)
        print('Dobro pozhalovat na nash resurs!')
    elif b == 'No':
        print('nu i ladno(')
f.close()
