# Первая задача
a = [50, 30, 14, 15, 1]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
# Первая задача альтернатива
a = [50, 20, 14, 5, 30, 1, 10]
x = 0
while x < len(a):
    j = 0
    while j < len(a)-1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
        j += 1
    x += 1
print(a)
# Вторая задача
x = 0
while x < 5:
    x += 1
    love = input('Введите ваше любимое число')
    if x <= 3 and love.isdigit() == True:
        print('good work')
        break
    elif x <= 3 and love.isdigit() != True:
        print('Будьте внимательнее и введите именно число')
    elif 3 < x <= 5 and love.isdigit() == True:
        print('good work')
        break
    else:
        print('Внимательнее будь!')
else:
    print('Последний шанс ввести любимое число!')
    love = input('Введите ваше любимое число')
    if love.isdigit() == True:
        print('good work')
    else:
        print('Иди лесом со своими промахами')
