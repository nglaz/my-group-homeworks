# берем ввод от пользователя
print('введи имя')
name = input()
print('введи пол')
sex = input()
print('введи ввозвраст')
age = input()
q_name = 'Hello! My name is '+name
q_age = '. I am '+age
q_sex = '. i am a '+sex
# создаем строку
all_text = q_name+q_age+q_sex
# создаем строку с %
all_text1 = 'Hello! My name is %s. ' 'I am %s .' 'I am a %s' %(name,age,sex)
# создаем строку с строчным методом
all_text2 = 'Hello! My name is {} .' 'I am {} .' 'I am a {}' .format(name,age,sex)
print(all_text)
print(all_text1)
print(all_text2)
# создаем строку с ф-строкой
about_me_fstring = F'Hello! My name is {name}. I am {age}. I am a {sex}'
print(about_me_fstring)

about_me_fstring_1 = F'Hello! My name is {name}. '
about_me_fstring_2 = F'I am {age}. '
about_me_fstring_3 = F'I am a {sex}'
print(about_me_fstring_1+about_me_fstring_2+about_me_fstring_3)

# данные о друге
print('введи имя друга')
name = input()
print('введи пол друга')
sex = input()
print('введи ввозвраст друга')
age = input()

# выводим данные о друге
print(about_me_fstring)
# из строки в список
list_from_str = list(about_me_fstring)
print(list_from_str)
# тип
print(type(list_from_str))

str_from_list = ','.join(list_from_str)
print(str_from_list)
print(type(str_from_list))

#
str_from_list = '. '.join(list_from_str)
print(str_from_list)
print(about_me_fstring.swapcase())
