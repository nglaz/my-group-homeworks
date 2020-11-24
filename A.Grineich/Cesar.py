alph = {'Latin.lower': 'abcdefghijklmnopqrstuvwxyz',
        'Latin.upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'Cyrillic.lower': 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
        'Cyrillic.upper': 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        'Numbers': '1234567890',
        'Symbols': ',.?!- :;"\'()*&^%$#@+/\\<>\n',
        }
origin = ''


def legere(action=''):

    while True:
        try:
            orig_file = str(input(F'What file would you want to {action} ("file.txt format")\n- '))
            with open(orig_file, encoding='utf8') as file:
                orig = file.read()
        except FileNotFoundError:
            print('There is no such file, try again.')
            continue
        else:
            break
    return orig


def cipher(shift=5):
    dec = ''
    for sym in origin:
        for bet in alph.values():
            if sym in bet:
                dec += bet[(bet.index(sym) + shift) % len(bet)]
    return dec


def scribo(name='', result=''):
    filename = str(input(F'In which file do you want to write result?      | "{name}" as default\n- '))
    if '.txt' in filename:
        print(F'Name of file - "{filename}"')
    else:
        filename = name
        print(F'Wrong type, your file will be named "{name}"')

    with open(filename, 'w', encoding='utf8') as file:
        file.write(result)


def subcinctus(default=5):
    try:
        shift = int(input(F'Enter the key (alphabet shift)                  |  {default} is default\n- '))
    except ValueError:
        shift = default
        print('Wrong type, the key will be default')
    return shift


while True:
    task = input('1 - Encrypt your text. \n2 - Decrypt file. \nX - Exit \n'
                 '__________________________________________________________________\n- ')
    if task == '1':
        origin = legere('encrypt')
        res = cipher(subcinctus())
        scribo('Encrypted.txt', res)
        break
    elif task == '2':
        origin = legere('decrypt')
        res = cipher(-subcinctus())
        scribo('Decrypted.txt', res)
        break
    elif str(task).lower() == 'x' or str(task).lower() == 'exit':
        print('Vale!')
        break
    else:
        print('I don\'t understand you *_*')
