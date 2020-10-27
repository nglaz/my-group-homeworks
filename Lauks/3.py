import string

name = 'Andriy' #input('Please enter your name')
age = '37' #input('Please enter your age')
height = '178' #input('Please eneter your height')

about_me = 'Hallo! My name is ' + age  + '. I\'m ' + age + '. I\'m ' + height + '.'
print(about_me)

about_me = 'Hallo! My name is %s. I\'m %s. I\'m %s.' % (name, age, height)
print(about_me)

about_me = 'Hallo! My name is {0}. I\'m {1}. I\'m {2}.' .format(name, age, height)
print(about_me)

about_me_fstring = f'Hallo! My name is {name}. I\'m {age}. I\'m {height}.'
print(about_me_fstring)

sentence1 = about_me_fstring.split('. ')[0] + '.'
print(sentence1)
sentence2 = about_me_fstring.split('. ')[1] + '.'
print(sentence2)
sentence3 = about_me_fstring.split('. ')[2]
print(sentence3)

about_myfr = about_me_fstring.replace('My', 'My friend\'s').replace('I\'m', 'He\'s')
print(about_myfr)

list_from_str = about_me_fstring.split()
print(type(list_from_str))

str_from_list = ' '.join(list_from_str)
print(str_from_list)

swap_register = about_me_fstring.swapcase()
print(swap_register)