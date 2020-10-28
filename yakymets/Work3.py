Val = "Valentyna"
print(Val)
age = "17"
print(age)
gender = "women."
print(gender)
W = 'Hello! My name is ' + Val + ' . I`m ' + age + ' and I`m a ' + gender
print(W)
Q = 'Hello! My name is %s . I`m %s and I`m a %s ' % (Val, age, gender)
print(Q)
R = "Hello! My name is {name} . I`m {a} and I`m a {g} ".format(name=Val, a=age,
                                                               g=gender)
print(R)
about_me_fstring = f'Hello! My name is {Val} . I`m {age} and I`m a {gender} '
print(about_me_fstring)
d = (about_me_fstring[:6])
print(d)
n = (about_me_fstring[7:29])
print(n)
o = (about_me_fstring[30:53])
print(o)
V = "Victoria"
a = "18"
g = "women"
about_me_fstring2 = f'Hello! My name is {V} . I`m {a} and I`m a {g} .'
print(about_me_fstring2)
list_from_str = about_me_fstring.split()
print(list_from_str)
print(type(list_from_str))
str_from_list = ' '.join(list_from_str)
print(str_from_list)
print(about_me_fstring.swapcase())

