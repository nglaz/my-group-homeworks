from random import randint

V = 13
a = []
def bubble(list):
    for i in range(V-1):
        for j in range(V-i-1):
            if list[j] > list[j +1]:
                list[j] , list[j + 1] = list[j + 1] , list[j]

for i in range(V):
    a.append(randint(1, 99))

print(a)
bubble(a)
print(a)