x = open("users.txt", "a+")
usersr = x.read()
x.seek(0)
loggin = input('ti zdeshnii stalker? (type yes or no,but id like too )').lower()
if loggin == 'yes':
    print('then write your name and key word')
    login = input('your name stalker')
    password = input('your key word')
if login in usersr:
    print("est takoi, govori slovo ili provalivai")
else:
    print("provalivai poka ne zastrelili")
if password in usersr:
    print("nu zahodi, ne priznal srazy")
else:
    print("vse ge nado teba horowo prouchit")
if loggin == 'no,but id like too':
         register = input\
             ('togda skagi kak teba zovyt i prydymai svoe slovo '
              '(type xorowo or ne nado eto mne)').lower()
         if register == 'xorowo':
             with x as file:
                 file.write('\n' + login)
                 file.write('' + password)
                 print("paren ti xorowii mozhesh otdohnyt u nas")
         elif loggin == 'ne nado eto mne':
             print("ny i vali, vsego xorowego")