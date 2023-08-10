OK=False
valor = float(input('Digite um Valor: '))
qtd200=0
qtd100=0
qtd50=0
qtd20=0
qtd10=0
qtd5=0
qtd2=0
qtd1=0
qtd050=0
qtd025=0
qtd005=0
while OK == False:
    print('OK')
    if valor % 200 == 0:
        valor-=200
        qtd200+=1
    elif valor % 100 == 0:
        valor-=100
        qtd100+=1
    elif valor % 50 == 0:
        valor-=50
        qtd50+=1
    elif valor % 20 == 0:
        valor-=20
        qtd20+=1
    elif valor % 10 == 0:
        valor-=10
        qtd10+=1
    elif valor % 5 == 0:
        valor-=5
        qtd5+=1
    elif valor % 2 == 0:
        valor-=2
        qtd2+=1
    elif valor % 1 == 0:
        valor-=1
        qtd1+=1
    elif valor % 0.50 == 0:
        valor-=0.50
        qtd050+=1
    elif valor % 0.25 == 0:
        valor-=0.25
        qtd025+=1
    elif valor % 0.10 == 0:
        valor-=0.10
        qtd010+=1
    elif valor % 0.05 == 0:
        valor-=0.05
        qtd005+=1
    if valor == 0:
        OK = True
print('Quantidade de notas de 200: ',qtd200)
print('Quantidade de notas de 100: ',qtd100)
print('Quantidade de notas de 50: ',qtd50)
print('Quantidade de notas de 20: ',qtd20)
print('Quantidade de notas de 10: ',qtd10)
print('Quantidade de notas de 5: ',qtd5)
print('Quantidade de notas de 2: ',qtd2)
print('Quantidade de moedas de 1: ',qtd1)
print('Quantidade de moedas de 50: ',qtd050)
print('Quantidade de moedas de 25: ',qtd025)
print('Quantidade de moedas de 5 centavos: ',qtd005)







