import math
def AsalSayi(x):
    sorgu = True
    if x == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                sorgu = False
                break
    return sorgu
i = 2
topla = 0
while True:
    print(i)
    if AsalSayi(i):
        topla += i
    if i == 2000000:
        break
    i += 1
print(topla)

