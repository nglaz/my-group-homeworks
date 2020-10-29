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
'''named = 'Sasha'
aged = '18'
sexd = 'man'''

