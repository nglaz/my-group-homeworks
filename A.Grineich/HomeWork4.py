# Пузырьковая сортировка:

bubble = [0, 6, 1, 5, 7, 3, 1, 6, 4, 8, 15]
print(bubble, ' - Исходный список чисел')
while True:
    check = 0
    for j in range(len(bubble) - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
    for x in range(1, len(bubble)):
        if bubble[x] >= bubble[x - 1]:
            check += 1
    if check == len(bubble) - 1:
        break
print(bubble, ' - Список обработанный пузырьковой сортировкой')

# Задача с любимым числом:

print('Введите любимое число:')
miscount = 0

while True:
    fav = input('- ')
    if fav.isdigit() is False:
        if miscount < 3:
            miscount += 1
            print('Я ведь просил число, будьте внимательнее.')
            continue
        elif 3 <= miscount < 5:
            miscount += 1
            print('Ты что сюда дурачиться ришёл? Давай вводи число!')
            continue
        elif fav.isdigit() is False and miscount == 5:
            print('Последний шанс! Вводи число, или проваливай!')
            miscount += 1
            continue
        else:
            print('Дефиченко какой-то! Сгинь!')
    break
