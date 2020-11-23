import string

alphabet = string.ascii_lowercase * 2
numbers = string.digits * 2
choice = int(input('Please enter 1 if you want to encrypt'
                   ' or 2 if you want to decrypt '))
if choice == 1:
    def encryption(text_file, key, encryption_file):
        result = ''
        with open(text_file) as file:
            text = file.read().lower()
        for symbol in text:
            new_position = alphabet.find(symbol) + key
            new_position_num = numbers.find(symbol) + key
            if symbol in alphabet:
                result = result + alphabet[new_position]
            elif symbol in numbers:
                result = result + numbers[new_position_num]
            else:
                result = result + symbol

        with open(encryption_file, 'w') as en_file:
            en_file.write(result)


    encryption(
        text_file=input('Please enter name of your file '),
        key=int(input('Please enter encryption key ')),
        encryption_file=input('Please enter name of encryption file ')
    )


elif choice == 2:
    def decryption(encryption_file, key, decryption_file):
        result = ''
        with open(encryption_file) as file:
            text = file.read().lower()
        for symbol in text:
            new_position = alphabet.find(symbol) - key
            new_position_num = numbers.find(symbol) - key
            if symbol in alphabet:
                result = result + alphabet[new_position]
            elif symbol in numbers:
                result = result + numbers[new_position_num]
            else:
                result = result + symbol

        with open(decryption_file, 'w') as file:
            file.write(result)


    decryption(
        encryption_file=input('Please enter name of encryption file '),
        key=int(input('Please enter decryption key ')),
        decryption_file=input('Please enter name of decryption file ')
    )



