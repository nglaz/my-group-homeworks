import string

alphabet = string.ascii_lowercase * 2
choice = int(input('Please enter 1 if you want to encrypt'
                   ' or 2 if you want to decrypt '))
if choice == 1:
    text_file = input('Please enter name of your file ')
    key = int(input('Please enter encryption key '))
    encryption_file = input('Please enter name of encryption file ')
    result = ''
    with open(text_file) as file:
        text = file.read().lower()
    for letter in text:
        new_position = alphabet.find(letter) + key
        if letter in alphabet:
            result = result + alphabet[new_position]
        else:
            result = result + letter

    with open(encryption_file, 'w') as en_file:
        en_file.write(result)

elif choice == 2:
    text_file = input('Please enter name of encryption file ')
    key = int(input('Please enter decryption key '))
    decryption_file = input('Please enter name of decryption file ')
    result = ''
    with open(text_file) as file:
        text = file.read().lower()
    for letter in text:
        new_position = alphabet.find(letter) - key
        if letter in alphabet:
            result = result + alphabet[new_position]
        else:
            result = result + letter

    with open(decryption_file, 'w') as en_file:
        en_file.write(result)
