import os
import datetime

data = datetime.date.today()

escolha=''
print(1+2)
while(escolha!='sair'):
    os.system('cls')
    nome = input('Digite um Nome: ')
    try:
        nascimento = int(input("Digite seu ano de nascimento: "))
        idade = data.year- nascimento

        print("Olá ",nome," Você tem ",idade, " Anos")

        escolha = input("Deseja Continuar? S/N \n")
        escolha = escolha.upper()

        if (escolha == "N"):
            escolha = "sair" 
        elif (escolha !="S"):
            print("Por Favor escolha uma das opções")
            os.system('pause')
    except:
        print("Por favor digite numeros")
        os.system('pause')


os.system('pause')

"""
   Na aula aprendemos sobre prints e comentarios em python 
   principalmente tiramos duvidas de como a linguagem funciona 
   Desenvolvemos apenas a saida de dados dos passos de desenvolvimento
   que são: Entrada, Processamento e Saida
 
"""