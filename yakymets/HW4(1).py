from random import randint

V = 13
a = []
for i in range(V):
    a.append(randint(1, 99))
print(a)

for i in range(V-1):
    for r in range(V-i-1):
        if a[r] > a[r +1]:
             a[r] , a[r + 1] = a[r + 1] , a[r]



print(a)
