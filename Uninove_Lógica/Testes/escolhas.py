import os
escolha = int(input('Escolha uma das opções \n1-calculo de média\n2-calculo de area\n3-calculo de idade\n0-sair\n'))
while (escolha!=0):
    if(escolha==1):
        print('Caluculo de Média')
        try:
            qtd = int(input('Digite a quantidade de elementos para adicionar: '))
            os.system('pause')
        except:
            print('Por favor digite numeros')
print('Saida do WHILE')
