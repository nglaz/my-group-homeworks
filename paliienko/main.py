N = 'alex'
a = '27'
k = 'female'
n1 = ('Hello! My name is alex.')
a2 = (''' I a'm 27 and i'm female''')
print(a2)
kon = (n1 + a2)
print(kon)
form = ("Hello! My name is %s. I a'm %d and i'm %s" % ('alex', 27, 'female'))
print(form)
form1 = ("Hello! My name is {}. I a'm {} and i'm {}"
         .format('alex', 27, 'female'))
print(form1)
about_me_fstring = (F"Hello! My name is {N}. i a'm {a} and i'm {k}")
m = (F"Hello! My name is {N}.")
z = (F"i a'm {a} and i'm {k}")
about = (m + z)
print(about)
list_from_str = (list(about_me_fstring))
print(list_from_str)
print(type(list_from_str))
str_from_list = (''.join(list_from_str))
print(str_from_list)
print(about_me_fstring.swapcase())

