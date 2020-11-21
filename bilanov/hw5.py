import string
# Homework 5 by Bilanov I.V.

# Реализуйте шифратор и дешифратор по шифру Цезаря.

# Спросить пользователя, что он хочет сделать - зашифровать или
# расшифровать файл.
answer = input('Welcome to Ceaser crypt. Do you want to encrypt or decrypt a '
               'file? Please type "en" to encrypt or "de" to decrypt.\n')
while answer != 'en' and answer != 'de':
    answer = input('please type "en" or "de" to encrypt or decrypt\n')

while True:
    key = input('enter a key in range 1-25: ')
    if key.isdigit() is False:
        print('please enter a NUMBER')
    else:
        if int(key) > 25 or int(key) < 1:
            print('please enter a valid number')
        else:
            print('key correct. continuing...')
            break


alphabet = string.ascii_letters


def encrypt(key=1):
    fileToEnCrypt = input('enter a file name you want to encrypt\n')
    fileEncrypted = input('enter a file name you want to save your encrypted '
                          'data\n')
    with open(f'{fileToEnCrypt}.txt', 'a+', encoding='utf-8') as fencrypt,\
        open(f'{fileEncrypted}.txt', 'a+', encoding='utf-8') as fencrypted:
        fencrypt.seek(0)
        tocrypt = fencrypt.read()
        for letter in tocrypt:
            position = alphabet.find(letter)
            newPosition = position + int(key)
            if letter in alphabet:
                fencrypted.write(alphabet[newPosition])
            else:
                fencrypted.write(letter)
    print(f'Your {fileToEnCrypt}.txt file has been encrypted and saved as'
          f' {fileEncrypted}.txt . Thanks for using our program)')


def decrypt(key=1):
    fileToDeCrypt = input('enter a file name you want to decrypt\n')
    fileDecrypted = input('enter a file name you want to save your decrypted '
                          'data\n')
    with open(f'{fileToDeCrypt}.txt', 'a+', encoding='utf-8') as fdecrypt,\
        open(f'{fileDecrypted}.txt', 'a+', encoding='utf-8') as fdecrypted:
        fdecrypt.seek(0)
        todecrypt = fdecrypt.read()
        for letter in todecrypt:
            position = alphabet.find(letter)
            newPosition = position - int(key)
            if letter in alphabet:
                fdecrypted.write(alphabet[newPosition])
            else:
                fdecrypted.write(letter)
    print(f'Your {fileToDeCrypt}.txt file has been encrypted and saved as'
          f' {fileDecrypted}.txt . Thanks for using our program)')



# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла,
# который мы получим на выходе(зашифрованного) и
# ключ(ключем будет уроваень сдвига).
if answer == 'en':
    encrypt(key)

# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на
# выходе(расшифрованного) и ключ.
else:
    decrypt(key)












