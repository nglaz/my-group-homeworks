import string
print('Vvedite pozhalusta sleduyushie dannie ')
name = str(input('Vashe imya : '))
age = str(input('Skolko vam let : '))
sex = str(input('Vash pol : '))
conc1 = 'Hello! My name is ' + str(name) + '. I\'m ' + str(age) + ', and I\'m a ' + str(sex) + '.'
print('Concatulyaciya : ', conc1)
f1 = 'Hello! My name is {0}. I\'m {1}, and i\'m a {2}.'.format(name, age, sex)
print('format : ', f1)
procent = 'Hello! My name is %s. I\'m %s, and i\'m a %s.' % (name, age, sex)
print('% : ', procent)
about_me_fstring = f'Hello! My name is {name}. I\'m {age}, and i\'m a {sex}.'
print('f-string : ', about_me_fstring)
str1 = about_me_fstring[:about_me_fstring.index('I')]
str2 = about_me_fstring[about_me_fstring.find('I'):about_me_fstring.rindex('I'):]
str3 = about_me_fstring[about_me_fstring.rindex('I'):]
print(str1, '\n', str2, str3)
about_friend_fstring = about_me_fstring.replace('Vanya', 'Masha').replace('20', '21').replace('man', 'woman')
print(about_friend_fstring)
list_from_str = about_me_fstring.split('. ')
print(list_from_str)
print(type(list_from_str))
str_from_list = '. '.join(list_from_str)
print(str_from_list)
print(about_me_fstring.swapcase())