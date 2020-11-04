import random
import string
print(random.randint(10 , 30))
bob = list(range ( 0 , 11))
print(bob)
red = list(string.ascii_letters)
print(red[:9])
green = list(string.ascii_letters)
print(green[10:26])
v = bob + red + green
print(v)
