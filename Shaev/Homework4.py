# Первая задача
x = 4
a = [50, 30, 14, 15, 1]
for i in range(x-1):
    for j in range(x-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
# Вторая задача
x = 0
while x < 5:
    x+=1
    love = input('Введите ваше любимое число')
    if x <= 3:
        if love.isdigit() == True:
            print('good work')
            break
        else:
            print('Будьте внимательнее и введите именно число')
    elif 3 < x <= 5:
        if love.isdigit() == True:
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