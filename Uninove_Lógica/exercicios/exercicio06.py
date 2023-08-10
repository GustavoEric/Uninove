import time
cont = int(input('Digite até que numero você quer contar: '))

x = 0

for x in range (cont):
    time.sleep(1)
    print(x+1,end=" ")