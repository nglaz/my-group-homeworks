# Task 1
from random import randint
number_list = [randint(-100, 100) for i in range(10)]
print(number_list)
for y in range(len(number_list)-1):
    for x in range(len(number_list)-y-1):
        if number_list[x] > number_list[x+1]:
            number_list[x], number_list[x+1] = number_list[x+1], number_list[x]
print(number_list)

# Task 2
count = 0
while True:
    favorite_num = input('Please enter your favorite number: ')
    if len(favorite_num) == 0:
        print('You have entered nothing')
        continue
    count += 1
    if favorite_num.isdigit() is True:
        print('Thanks!')
        break
    elif count == 7 and favorite_num.isdigit() is False:
        print('You are an idiot! Have a nice day')
        break
    elif count > 5 and favorite_num.isdigit() is False:
        print('You have the last chance')
    elif 3 < count <= 5 and favorite_num.isdigit() is False:
        print('It is not a number too, you should to think')
    elif count <= 3 and favorite_num.isdigit() is False:
        print('It is not a number!')








