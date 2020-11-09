x = open("users.txt", "a+")
x.seek(0)
usersr = x.read().split()
loggin = input('are you signed? (type yes or no)').lower()
if loggin == 'yes':
    print('write login and password')
    login = input('your name')
    if login in usersr:
        print('good')
    else:
        print('not good')
    password = input('password')
    x.seek(0)
    if password in usersr:
        print('good')
    else:
        print('not good')
elif loggin == 'no':
    register = input\
             ('pridymai log i password'
              '(type ok or ne)').lower()
    if register == 'ok':
        login = input("log")
        password = input("pass")
        with x as file:
            file.write('\n' + login)
            file.write(' ' + password)
        print('good')
    elif loggin == 'ne':
        print('not good')
x.close()