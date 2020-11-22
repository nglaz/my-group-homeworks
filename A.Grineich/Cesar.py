from string import ascii_letters

alph = ascii_letters + ' ,.!?-'
print(alph)


def encrypt_file(shift=5):

    while True:
        try:
            orig_file = str(input('What file would you want to encrypt ("file.txt format")\n- '))
            with open(orig_file) as file:
                orig = file.read().replace('\n', ' ')
        except FileNotFoundError:
            print('There is no such file, try again.')
            continue
        else:
            break

    print(orig)

    encd_file = input('Type name of the file ("file.txt" format)       |  "Encrypted.txt" as default\n- ')

    if '.txt' in encd_file:
        print('Name of file - ', encd_file)
    else:
        encd_file = 'Encrypted.txt'
        print('Wrong type, your file will be named "Encrypted.txt"')

    try:
        shift = int(input('Enter the key (alphabet shift)                  |  ' + str(shift) + ' is default\n- '))
    except ValueError:
        print('Wrong type, the key will be default')

    encd = ''

    with open(encd_file, 'w') as file:

        for s in orig:
            encd += alph[(alph.index(s) + shift) % len(alph)]
        file.write(encd)


def decrypt_file(shift=5):
    while True:
        try:
            orig_file = str(input('What file would you want to decrypt ("file.txt format")\n- '))
            with open(orig_file) as file:
                orig = file.read().replace('\n', ' ')
        except FileNotFoundError:
            print('There is no such file, try again.')
            continue
        else:
            break

    print(orig)

    decd_file = input('Type name of the file ("file.txt" format)       |  "Decrypted.txt" as default\n- ')

    if '.txt' in decd_file:
        print('Name of file - ', decd_file)
    else:
        decd_file = 'Decrypted.txt'
        print('Wrong type, your file will be named "Decrypted.txt"')

    try:
        shift = int(input('Enter the key (alphabet shift)                  |  ' + str(shift) + ' is default\n- '))
    except ValueError:
        print('Wrong type, the key will be default')

    decd = ''

    with open(decd_file, 'w') as file:

        for s in orig:
            decd += alph[(alph.index(s) + len(alph) - shift) % len(alph)]
        file.write(decd)


while True:
    task = input('1 - Encrypt your text. \n2 - Decrypt file. \nX - Exit \n'
                 '__________________________________________________________________\n- ')
    if task == '1':
        encrypt_file()
    elif task == '2':
        decrypt_file()
    elif str(task).lower() == 'x' or str(task).lower() == 'exit':
        print('Vale!')
        break
    else:
        print('I don\'t understand you *_*')
