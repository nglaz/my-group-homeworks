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
    key1 = input('enter a key in range 1-25: ')
    if key1.isdigit() is False:
        print('please enter a NUMBER')
    else:
        if int(key1) > 25 or int(key1) < 1:
            print('please enter a valid number')
        else:
            print('key correct. continuing...')
            break


alphabet = string.ascii_letters
digits = string.digits + string.digits


def encrypt(key=1):
    file_to_encrypt = input('enter a file name you want to encrypt\n')
    file_encrypted = input('enter a file name you want to save your '
                           'encrypted data\n')
    try:
        with open(f'{file_to_encrypt}.txt', 'r+', encoding='utf-8') as \
                fencrypt, open(f'{file_encrypted}.txt', 'a+',
                               encoding='utf-8') as fencrypted:
            fencrypt.seek(0)
            tocrypt = fencrypt.read()
            for letter in tocrypt:
                position = alphabet.find(letter)
                newposition = position + int(key)
                if letter in alphabet:
                    fencrypted.write(alphabet[newposition])
                elif letter in digits:
                    dposition = digits.find(letter)
                    newdposition = dposition + int(key)
                    fencrypted.write(digits[newdposition])
                else:
                    fencrypted.write(letter)
        print(f'Your {file_to_encrypt}.txt file has been encrypted and saved '
              f'as {file_encrypted}.txt . Thanks for using our program)')
    except FileNotFoundError:
        print(f'File {file_to_encrypt}.txt not found. Try again...')


def decrypt(key=1):
    file_to_decrypt = input('enter a file name you want to decrypt\n')
    file_decrypted = input('enter a file name you want to save your decrypted '
                           'data\n')
    try:
        with open(f'{file_to_decrypt}.txt', 'r+', encoding='utf-8') as \
                fdecrypt, open(f'{file_decrypted}.txt', 'a+',
                               encoding='utf-8') as fdecrypted:
            fdecrypt.seek(0)
            todecrypt = fdecrypt.read()
            for letter in todecrypt:
                position = alphabet.find(letter)
                newposition = position - int(key)
                if letter in alphabet:
                    fdecrypted.write(alphabet[newposition])
                elif letter in digits:
                    dposition = digits.find(letter)
                    newdposition = dposition - int(key)
                    fdecrypted.write(digits[newdposition])
                else:
                    fdecrypted.write(letter)
        print(f'Your {file_to_decrypt}.txt file has been encrypted and saved '
              f'as {file_decrypted}.txt . Thanks for using our program)')
    except FileNotFoundError:
        print(f'File {file_to_decrypt}.txt not found. Try again...')


# Если зашифровать, попросить у него ввести имя шифруемого файла, имя файла,
# который мы получим на выходе(зашифрованного) и
# ключ(ключем будет уроваень сдвига).
if answer == 'en':
    encrypt(int(key1))

# Если расшифровать, попросить ввести имя зашифрованного файла, имя файла на
# выходе(расшифрованного) и ключ.
else:
    decrypt(int(key1))
