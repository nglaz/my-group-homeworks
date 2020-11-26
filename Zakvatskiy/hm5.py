from string import ascii_letters as a_l


alpha = a_l+' '
name = input('введи файл с которым будем роботать: ')
new_name_file = input('введи имя будущего файла: ')


def encryption(d_t_string, type_n, new_name=new_name_file, def_name=name):
    res = ''
    with open(new_name, 'a') as f, open(def_name, 'r+') as f1, \
            open('f.txt', 'a+') as f2:
        read_file = f1.read()
        for c in read_file:
            res += d_t_string[(d_t_string.index(c) + type_n) % len(d_t_string)]
        f.write(res)
        f2.write(f.name+' '+str(type_n)+' \n')


def decryption(inp_name=name):
    with open('f.txt', 'r+') as f:
        read_f = f.read().replace(' \n', ' ').split()
        print(read_f)
        if inp_name in read_f:
            for elem in read_f[1]:
                encryption(alpha, -int(elem))


user_des = input('зашифровать , или наоборот (ответ: 1 , 2, stop):')
if user_des == '1':
    while True:
        key = int(input('введи ключ: '))
        try:
            encryption(alpha, key)
        except FileNotFoundError:
            print('Неправильный ввод:(')
        else:
            break
elif user_des == '2':
    decryption()