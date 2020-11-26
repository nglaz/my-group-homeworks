import string

process = input('Type "encrypt" if you wish to encrypt your file or "decrypt" '
                'if you wish to decrypt your file.').lower().strip()
if process == 'encrypt' or process == 'decrypt':
    pass
else:
    print('You have entered wrong option, please check and run the program again')
    exit()

def source():
    source = input('Please enter source file name') + '.txt'

    def file_read(*args):
        try:
            with open(source, 'r+', encoding='UTF8') as file:
                content = file.read()
                file.close()
        except FileNotFoundError:
            print('No such source file, please check and run the program again')
            exit()
        return content

    def result():
        result = input('Please enter result file name') + '.txt'

        return result

    def file_write(*args):

        def key():
            key = input('Please enter a number for encryption key')
            try:
                key = int(key)
            except ValueError:
                while key.isdigit() == False:
                    key = input('You entered not a valid number, please try again')
            key = int(key)
            while key >= len(sample):
                key = int(input('The key you entered is too big, please enter smaller one'))

            return key

        sample = string.ascii_letters

        def encrypt(*args):
            output = ''.join(list(map(lambda letter: sample[sample.index(letter) - key]
            if letter in sample else letter, file_read())))
            return output

        def decrypt(*args):
            output = ''.join(list(map(lambda letter: sample[sample.index(letter)
            + key - len(sample)] if letter in sample else letter, file_read())))
            return output

        with open(result(), 'w+', encoding='UTF8') as file:
            key = key()
            if process == 'encrypt':
                print(encrypt(), file=file)
            elif process == 'decrypt':
                print(decrypt(), file=file)
            file.close()

    file_write()
    return source


source()