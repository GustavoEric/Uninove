import datetime

data = datetime.date.today()
notas = []
media=0
print(data.strftime("%d/%m/%y"))
quantidade= int(input("Quantas Notas Você Vai somar?: "))
for x in range(quantidade):
    nota = float(input("Digite nota "+str(x+1)+": "))
    notas.append(nota)
    x+=1

for y in notas:
    media+=y

media=media/quantidade

print("Media: ",media)
print(notas)
#nota = 7.8

#print(int(nota))
#print(float(nota))
#print(str(nota))