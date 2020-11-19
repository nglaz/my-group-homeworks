from random import randint

num = 10
a = []
for i in range(num):
    a.append(randint(1, 10))
print(a)

for i in range(num - 1):
    for j in range(num - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

num_i = 0
while True:
    liked_num = input('Введи любимое число: ')
    if liked_num.isdigit() is True:
        print('Спасибо за сотрудничество :)')
        break
    else:
        num_i += 1
        if 3 <= num_i < 5:
            print('Введите ЧИСЛО!!!')
        elif num_i == 5:
            print('Последний шанс')
        elif num_i < 3:
            print('Будьте болие внимательны, введите число')
        else:
            print('ИДИ ЛЕСОМ!')
            break
        continue
