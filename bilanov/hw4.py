import random
# Homework4 by Bilanov
# Zadacha1 (puzirkovaya sortirovka)
# for
d = []

for i in range(11):
    d.append(random.randint(1, 100))

print(d)

for i in range(11):
    for x in range(11 - i - 1):
        if d[x] > d[x+1]:
            d[x], d[x+1] = d[x+1], d[x]

print('for : ', d)

# while
d1 = []
for i in range(11):
    d1.append(random.randint(1, 100))

print(d1)

x = 0
while x < 10:
    y = 0
    while y < 10 - x:
        if d1[y] > d1[y+1]:
            d1[y], d1[y+1] = d1[y+1], d1[y]
        y += 1
    x += 1


print('while : ', d1)

# Zadacha2 ili proverka na tupogo polzovatelya)
i = 0
while True:
    i += 1
    a = input('Vvedite svoe lyubimoe chislo : ')
    if a.isdigit():
        print('Molodec, otlichno srabotano!')
        break
    elif a.isdigit() is False:
        if i > 0 and i < 3:
            print('Poprobuyte eshe raz, pozhaluista)')
        if i >= 3 and i < 5:
            print('Ti mozhesh vvesti chislo ili ti sovsem tupoi?')
        if i == 5:
            print('Dayu posledniy shans ili cikl zakonchitsa prinuditelno, '
                  'ne nado tak! ')
        if i == 6:
            print('Nu ti i tupoi!')
            break