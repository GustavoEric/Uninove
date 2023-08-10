import random
i = 0
a = [1,2,3,4,5,6,7,8,9,10]
for i in a: 
    pA = random.randint(1,10)
    pB = random.randint(1,10)
    o = random.randint(1,3)
    if (o == 1):
        print('Submarino Posição: ',pA,pB)
        a.remove(pA)
    if (o == 2):
        print('Agua Posição: ',pA,pB)
    if (o == 3):
        print('Destroyer Posição: ',pA,pB)