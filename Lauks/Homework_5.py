# Task "Caesar's Cypher"

import string

sample = string.printable

def encrypt(*args):
    output = ''.join(list(map(lambda letter: sample[sample.index(letter) - int(key)], content)))
    return output


def decrypt(*args):
    output = ''.join(list(map(lambda letter: sample[sample.index(letter) + int(key)  - len(sample)],\
                              content)))
    return output


def processing(*args):
    with open(source, 'r+', encoding='UTF8') as file:
        global content
        content = file.read()
        file.close()
    with open(result, 'w+', encoding='UTF8') as file:
        if process == 'encrypt':
            print(encrypt(content), file=file)
        else:
            print(decrypt(content), file=file)
        file.close()
    return


def user_input():
    global process
    process = input('Type "encrypt" if you wish to encrypt your file or "decrypt" if '
        'you wish to decrypt your file.').lower().strip()
    if process == 'encrypt' or process == 'decrypt':
        global source, result, key
        source, result, key = input('''Please enter: \nsource file name, 
result file name \nand the key, \nall separated with "space".''').split()
        processing()
    else:
        print('Wrong answer')
        user_input()
    return process, source, result, key

user_input()