import time
import sys
import os

nomes = ['Gustavo','Gabriel','Pablo','Gustavo']

escolha = input('Digite um Nome: ')

def animate():
    simbolos = ['|','/','-','\\','|','/','-','\\']
    for c in simbolos:
        os.system('cls')
        print('Loading ',c)
        time.sleep(1)
try:
    indice = nomes.index(escolha)
    contagem = nomes.count(escolha)
    print(nomes[indice])
    print(f'O nome {escolha} apareceu {contagem} vez(es)')
    txt = input('Digite um Texto:')
    list_txt = list(txt)
    list_txt.reverse()
    print(list_txt)
    print(txt.replace('P', 'Q'))
    animate()
    reverso = "".join(list_txt)
    print(reverso)
except:
    print('Nome não encontrado')