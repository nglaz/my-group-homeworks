# name = 'Anton'
# age = '22'
# gender = 'male'
name = input('Name is - ')
age = input('Age is - ')
gender = input('Gender is - ')

str_1 = 'Hello, my name is ' + name + '. ' + 'I\'m ' + age + ' and I\'m a '\
        + gender.lower() + '.'
print(str_1, ' - Concatenated')

print('Hello, my name is %(1)s. I\'m %(2)s and I\'m a %(3)s.'
      % {'1': name, '2': age, '3': gender.lower()}, ' - % formatting')

# % formatting sucks

str_2 = 'Hello, my name is {}. I\'m {} and I\'m a {}.'\
    .format(name, age, gender.lower())
print(str_2, ' - Formatting metod')


about_me_fstring = \
    f'Hello, my name is {name}. I\'m {age} and I\'m a {gender.lower()}.'

print(about_me_fstring, ' - F-string')

x = about_me_fstring.index('.')  # variable made to split sentences

sent_1 = about_me_fstring[:x + 1]
sent_2 = about_me_fstring[x + 2:]

print(sent_1, ' - First sentence out of full string',
      '\n',  sent_2, ' - Second sentence out of full string')

print(about_me_fstring.replace(name, 'Pasha').replace(age, '25')
      .replace(gender, 'male'), ' - Changed with friends parameters')

list_from_str = about_me_fstring.split('.')

print(list_from_str, ' - List from str\n',
      type(list_from_str))

a = (list_from_str[0])
b = (list_from_str[1])
str_from_list = f'{a}.{b}.'
print(str_from_list, ' - String from list')

print(about_me_fstring.swapcase(), ' - Change register')
