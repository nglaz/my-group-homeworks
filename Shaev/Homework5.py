import string
lexicon = chr(32) + string.ascii_letters + string.digits + string.punctuation


def cezar(codefile, key, newcodefile):
    with open(codefile, 'r+', encoding='utf-8') as f:
        text = f.read()
        for word in text:
            for letter in word:
                with open(newcodefile, 'a+', encoding='utf-8') as f1:
                    if letter in lexicon:
                        loc = lexicon.find(letter)
                        letter = lexicon[loc + key]
                        f1.write(letter)
                    elif letter == '\n':
                        lexicon == '\n'
                        f1.write(letter)
                    else:
                        loc = lexicon.find(letter)
                        new_letter = lexicon[loc + key]
                        f1.write(new_letter)


def uncezar(codefile, key, newcodefile):
    with open(codefile, 'r+', encoding='utf-8') as f:
        a = f.read()
        for word in a:
            for letter in word:
                with open(newcodefile, 'a+', encoding='utf-8') as f1:
                    if letter in lexicon:
                        loc = lexicon.find(letter)
                        letter = lexicon[loc - key]
                        f1.write(letter)
                    elif letter == '\n':
                        lexicon == '\n'
                        f1.write(letter)
                    else:
                        loc = lexicon.find(letter)
                        new_letter = lexicon[loc - key]
                        f1.write(new_letter)


def question():
    answer = input('Здравствуйте, вы желаете зашифровать или расшифровать файл? [code] [encode]').lower()
    try:
        if answer == 'code':
            cezar(input('Введите имя шифруемого файла [.txt]'),
                  int(input('Введите ключ шифровки от 1 до 25')),
                  input('Введите имя файла с будущим шифром [.txt]'))
        elif answer == 'encode':
            uncezar(input('Введите имя зашифрованого файла [.txt]'),
                    int(input('Введите ключ шифровки от 1 до 25')),
                    input('Введите имя файла с будущей расшифровкой [.txt]'))
        else:
            print('Введиьте корректное название')
    except FileNotFoundError:
        print('Введите корректное имя файла! [.txt]')
    except IndexError:
        print('Введите от 1 до 25!')
    except ValueError:
        print('Введите именно число!')


question()
