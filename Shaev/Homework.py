print('Введите имя, возраст и пол поочерёдно: \n')
name = input()
age = input()
gender = input()
print('Hello my name is ' '{}' ', I\'m ' '{}' ', and I\'m a ' '{}'.format(name, age, gender))
formats = 'Hello my name is ' "%s" ', I\'m ' "%s" ', and I\'m a ' "%s" % (name, age, gender)
print(formats)
about_me_fstring = f"Hello my name is {name}, I\'m {age}, and I\'m a {gender}"
print(about_me_fstring)
print(about_me_fstring)
a = about_me_fstring.split(',')[0]
b = about_me_fstring.split(',')[1]
d = about_me_fstring.split(',')[2]
print(a, b, d)
list_from_str = about_me_fstring.split(',')
print(type(list_from_str))
str_from_list = ' '.join(list_from_str)
print(about_me_fstring.swapcase())
