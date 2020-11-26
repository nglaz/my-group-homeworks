import string
choice = int(input('Please enter 1 if you want to encrypt'
                   ' or 2 if you want to decrypt '))


def encryption(text_file, key, encryption_file):
    result = ''
    try:
        with open(text_file) as file:
            text = file.read()
        for item in text:
            alphabet = string.ascii_lowercase * (key + 1)
            alphabet_up = string.ascii_uppercase * (key + 1)
            numbers = string.digits * (key + 1)
            symbols = string.punctuation * (key + 1)
            new_position = alphabet.find(item) + key
            new_position_alphabet_up = alphabet_up.find(item) + key
            new_position_num = numbers.find(item) + key
            new_position_sym = symbols.find(item) + key
            if item in alphabet:
                result = result + alphabet[new_position]
            elif item in alphabet_up:
                result = result + alphabet_up[new_position_alphabet_up]
            elif item in numbers:
                result = result + numbers[new_position_num]
            elif item in symbols:
                result = result + symbols[new_position_sym]
            else:
                result = result + item

            with open(encryption_file, 'w') as en_file:
                en_file.write(result)
    except FileNotFoundError:
        print('There is no such file')
        encryption(
            text_file=input('Please enter name of your file '),
            key=int(input('Please enter encryption key ')),
            encryption_file=input('Please enter name of encryption file ')
        )


def decryption(encryption_file, key, decryption_file):
    result = ''
    try:
        with open(encryption_file) as file:
            text = file.read()
        for item in text:
            alphabet = string.ascii_lowercase * (key + 1)
            alphabet_up = string.ascii_uppercase * (key + 1)
            numbers = string.digits * (key + 1)
            symbols = string.punctuation * (key + 1)
            new_position = alphabet.find(item) - key
            new_position_alphabet_up = alphabet_up.find(item) - key
            new_position_num = numbers.find(item) - key
            new_position_sym = symbols.find(item) - key
            if item in alphabet:
                result = result + alphabet[new_position]
            elif item in alphabet_up:
                result = result + alphabet_up[new_position_alphabet_up]
            elif item in numbers:
                result = result + numbers[new_position_num]
            elif item in symbols:
                result = result + symbols[new_position_sym]
            else:
                result = result + item

            with open(decryption_file, 'w') as file:
                file.write(result)
    except:
        print('There is no such file')
        decryption(
            encryption_file=input('Please enter name of encryption file '),
            key=int(input('Please enter decryption key ')),
            decryption_file=input('Please enter name of decryption file ')
        )


if choice == 1:
    encryption(
        text_file=input('Please enter name of your file '),
        key=int(input('Please enter encryption key ')),
        encryption_file=input('Please enter name of encryption file ')
    )
elif choice == 2:
    decryption(
        encryption_file=input('Please enter name of encryption file '),
        key=int(input('Please enter decryption key ')),
        decryption_file=input('Please enter name of decryption file ')
    )


