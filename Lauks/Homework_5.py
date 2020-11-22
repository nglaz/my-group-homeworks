# Task "Caesar's Cypher"

import string

source = string.printable

def encrypt(*kwargs):
    output = ''.join(list(map(lambda letter: source[source.index(letter) - int(key)], content)))
    return output


def decrypt(*kwargs):
    output = ''.join(list(map(lambda letter: source[source.index(letter) + int(key)  - len(source)],\
                              content)))
    return output

choice = input('Type "encrypt" if you wish to encrypt your file or "decrypt" if '
               'you wish to decrypt your file.').lower().strip()

if choice == 'encrypt':
    input_file, output_file, key = input('''Please enter: \ndecrypted file name,
encrypted file name \nand the key, \nall separated with "space".''').split()
    with open(input_file, 'r+', encoding='UTF8') as file:
        content = file.read()
        file.close()
    with open(output_file, 'w+', encoding='UTF8') as file:
        file.write(encrypt(content))
        file.close()

elif choice == 'decrypt':
    input_file, output_file, key = input('''Please enter: \nencrypted file name, 
decrypted file name \nand the key, \n all separated with "space".''').split()
    with open(input_file, 'r+', encoding='UTF8') as file:
        content = file.read()
        file.close()
    with open(output_file, 'w+', encoding='UTF8') as file:
        file.write(decrypt(content))
        file.close()
else:
    print('Wrong answer')