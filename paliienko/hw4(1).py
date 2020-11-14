from random import randint
quantity = 10
bubles = []
for i in range(quantity):
    bubles.append(randint(1, 99))
print(bubles)
index = 0
while index < quantity - 1:
    j = 0
    while j < quantity - 1 - index:
        if bubles[j] > bubles[j+1]:
            bubles[j], bubles[j+1] = bubles[j+1], bubles[j]
        j += 1
    index += 1
print(bubles)


quantity = 10
bubles = []
for i in range(quantity):
    bubles.append(randint(1, 99))
print(bubles)
for i in range(quantity-1):
    for j in range(quantity-i-1):
        if bubles[j] >  bubles[j+1]:
            bubles[j], bubles[j+1] = bubles[j+1], bubles[j]
print(bubles)