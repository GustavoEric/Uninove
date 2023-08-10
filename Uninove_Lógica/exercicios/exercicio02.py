valor = float(input('Digite Um valor: '))
desconto = float(input('Digite o Desconto: '))
desconto = (100 - desconto)/100
print('Valor: ',valor)
print('Valor com Desconto: ',str(valor*desconto))