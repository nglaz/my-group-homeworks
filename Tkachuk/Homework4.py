# Task 1
from random import randint
number_list = [randint(-100, 100) for i in range(5)]

print(number_list)
while True:
    if number_list[0] > number_list[1]:
        number_list[0], number_list[1] = number_list[1], number_list[0]
    elif number_list[1] > number_list[2]:
        number_list[1], number_list[2] = number_list[2], number_list[1]
    elif number_list[2] > number_list[3]:
        number_list[2], number_list[3] = number_list[3], number_list[2]
    elif number_list[3] > number_list[4]:
        number_list[3], number_list[4] = number_list[4], number_list[3]
    else:
        break
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
    elif count == 6 and favorite_num.isdigit() is False:
        print('You have the last chance!')
    elif count == 5 and favorite_num.isdigit() is False:
        print('Numbers look like this -> 0 1 2 3 4 5 6 7 8 9')
    elif count == 4 and favorite_num.isdigit() is False:
        print('Are you serious?')
    elif count == 3 and favorite_num.isdigit() is False:
        print('Do you know what is it a number? '
              'You entered the letter! Try more')
    elif count == 2 and favorite_num.isdigit() is False:
        print('It is not a number too,'
              ' you should to think')
    elif count == 1 and favorite_num.isdigit() is False:
        print('It is not a number!')


