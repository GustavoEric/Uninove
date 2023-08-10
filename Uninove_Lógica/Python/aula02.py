import os 
import datetime
data = datetime.date.today()

#Entrada de dados 
nome = input("Digite seu Nome: ")
idade = int(input("Digite o Ano que voce Nasceu: "))
idade = data.year-idade

print(f"Você tem {idade} Anos")
if (idade >=18):
    print("Você pode Dirigir")
else:
    print("Você não pode Dirigir")
#print("Nome: ",nome," Idade: ",idade," Nota: ",nota)
os.system('pause')