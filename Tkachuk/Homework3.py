question = input('Do you have an account? \n"yes/no" ')
if question == 'yes':
    login = input("enter your login: ")
    password = input("enter your password: ")
    if login == "User123" and password == "qwerty":
        print('Access is allowed')
    else:
        print("Your login or password is not correct")
else:
    question2 = input('do you want to create an account? \n"yes/no" ')
    if question2 == 'yes':
        new_login = input("enter your login: ")
        new_password = input("enter your password: ")
        with open('users.txt', 'w') as users:
            users.write('login - ' + new_login + '\n'
            + 'password - ' + new_password)
        print('Your account has been created')
    else:
        print('Good luck!')
